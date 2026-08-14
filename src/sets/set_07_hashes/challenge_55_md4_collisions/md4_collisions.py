"""Cryptopals challenge 55: demonstrate Wang's MD4 collision differential.

The module contains the message differential from Wang et al. and the
first-round message modification used by the attack. Running the module
verifies a published collision pair using the sibling :mod:`md4` module.

MD4 is obsolete and must not be used for security-sensitive applications.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
import struct

if __package__:
    from .md4 import (
        INITIAL_STATE,
        MASK_32,
        ROUND_SHIFTS,
        TARGET_ORDER,
        left_rotate,
        md4,
        md4_f,
        right_rotate,
        self_test as md4_self_test,
        step_inputs,
    )
else:  # Support running this file directly as a script.
    from md4 import (
        INITIAL_STATE,
        MASK_32,
        ROUND_SHIFTS,
        TARGET_ORDER,
        left_rotate,
        md4,
        md4_f,
        right_rotate,
        self_test as md4_self_test,
        step_inputs,
    )


TARGET_NAMES = ("a", "b", "c", "d")


# The first-round portion of Table 6 in Wang et al. Bit positions are
# intentionally one-based to match the paper. A string value copies the named
# state's bit at the same position; a tuple can select a different bit.
BitSource = int | str | tuple[str, int]
FIRST_ROUND_CONSTRAINTS: dict[str, dict[int, BitSource]] = {
    "a1": {7: "b0"},
    "d1": {7: 0, 8: "a1", 11: "a1"},
    "c1": {7: 1, 8: 1, 11: 0, 26: "d1"},
    "b1": {7: 1, 8: 0, 11: 0, 26: 0},
    "a2": {8: 1, 11: 1, 14: "b1", 26: 0},
    "d2": {14: 0, 19: "a2", 20: "a2", 21: "a2", 22: "a2", 26: 1},
    "c2": {13: "d2", 14: 0, 15: "d2", 19: 0, 20: 0, 21: 1, 22: 0},
    "b2": {13: 1, 14: 1, 15: 0, 17: "c2", 19: 0, 20: 0, 21: 0, 22: 0},
    "a3": {
        13: 1,
        14: 1,
        15: 1,
        17: 0,
        19: 0,
        20: 0,
        21: 0,
        22: 1,
        23: "b2",
        26: "b2",
    },
    "d3": {
        13: 1,
        14: 1,
        15: 1,
        17: 0,
        20: 0,
        21: 1,
        22: 1,
        23: 0,
        26: 1,
        30: "a3",
    },
    "c3": {17: 1, 20: 0, 21: 0, 22: 0, 23: 0, 26: 0, 30: 1, 32: "d3"},
    "b3": {20: 0, 21: 1, 22: 1, 23: "c3", 26: 1, 30: 0, 32: 0},
    "a4": {23: 0, 26: 0, 27: "b3", 29: "b3", 30: 1, 32: 0},
    "d4": {23: 0, 26: 0, 27: 1, 29: 1, 30: 0, 32: 1},
    "c4": {19: "d4", 23: 1, 26: 1, 27: 0, 29: 0, 30: 0},
    "b4": {19: 0, 26: 1, 27: 1, 29: 1, 30: 0},
}


# First collision in Table 3 of Wang et al. The paper prints the 32-bit words
# as hexadecimal integers; MD4 serializes each word in little-endian order.
REFERENCE_WORDS = (
    0x4D7A9C83,
    0x56CB927A,
    0xB9D5A578,
    0x57A7A5EE,
    0xDE748A3C,
    0xDCC366B3,
    0xB683A020,
    0x3B2A5D9F,
    0xC69D71B3,
    0xF9E99198,
    0xD79F805E,
    0xA63BB2E8,
    0x45DD8E31,
    0x97E31FE5,
    0x2794BF08,
    0xB9E8C3E9,
)
REFERENCE_DIGEST = "4d7e6a1defa93d2dde05b45d864c429b"


def _bit(value: int, position: int) -> int:
    """Read a one-based bit position, matching the notation in Wang et al."""
    if not 1 <= position <= 32:
        raise ValueError("bit positions must be between 1 and 32")
    return (value >> (position - 1)) & 1


def _set_bit(value: int, position: int, bit: int) -> int:
    mask = 1 << (position - 1)
    return (value | mask) if bit else (value & ~mask)


def _expected_bit(source: BitSource, position: int, states: Mapping[str, int]) -> int:
    if isinstance(source, int):
        return source
    if isinstance(source, tuple):
        state_name, source_position = source
        return _bit(states[state_name], source_position)
    return _bit(states[source], position)


def _force_constraints(
    value: int,
    constraints: Mapping[int, BitSource],
    states: Mapping[str, int],
) -> int:
    for position, source in constraints.items():
        value = _set_bit(value, position, _expected_bit(source, position, states))
    return value & MASK_32


def _first_round_states(words: Sequence[int]) -> dict[str, int]:
    """Return the named a1, d1, ..., b4 state words for one block."""
    state = list(INITIAL_STATE)
    states = dict(zip(("a0", "b0", "c0", "d0"), state))
    for step, word in enumerate(words):
        target = TARGET_ORDER[step % 4]
        x, y, z = step_inputs(state, target)
        state[target] = left_rotate(
            state[target] + md4_f(x, y, z) + word,
            ROUND_SHIFTS[0][step % 4],
        )
        label = f"{TARGET_NAMES[target]}{step // 4 + 1}"
        states[label] = state[target]
    return states


def first_round_constraints_hold(block: bytes) -> bool:
    """Return whether a 64-byte block satisfies Wang's round-one conditions."""
    if len(block) != 64:
        raise ValueError("Wang's differential operates on one 64-byte block")
    states = _first_round_states(struct.unpack("<16I", block))
    return all(
        _bit(states[label], position) == _expected_bit(source, position, states)
        for label, constraints in FIRST_ROUND_CONSTRAINTS.items()
        for position, source in constraints.items()
    )


def massage_first_round(block: bytes) -> bytes:
    """Modify a block so every first-round condition in Wang's path holds.

    Each MD4 message word is used exactly once, in order, during round one.
    After forcing the required bits of an intermediate state, the corresponding
    word is recovered by inverting that MD4 step. Later steps therefore see the
    corrected state without invalidating earlier constraints.
    """
    if len(block) != 64:
        raise ValueError("Wang's differential operates on one 64-byte block")

    words = list(struct.unpack("<16I", block))
    state = list(INITIAL_STATE)
    states = dict(zip(("a0", "b0", "c0", "d0"), state))

    for step in range(16):
        target = TARGET_ORDER[step % 4]
        x, y, z = step_inputs(state, target)
        shift = ROUND_SHIFTS[0][step % 4]
        label = f"{TARGET_NAMES[target]}{step // 4 + 1}"

        value = left_rotate(state[target] + md4_f(x, y, z) + words[step], shift)
        corrected = _force_constraints(value, FIRST_ROUND_CONSTRAINTS[label], states)
        words[step] = (right_rotate(corrected, shift) - state[target] - md4_f(x, y, z)) & MASK_32
        state[target] = corrected
        states[label] = corrected

    result = struct.pack("<16I", *words)
    if not first_round_constraints_hold(result):
        raise AssertionError("internal error: first-round message modification failed")
    return result


def apply_wang_differential(block: bytes) -> bytes:
    """Create M' from M using Wang's three-word modular differential."""
    if len(block) != 64:
        raise ValueError("Wang's differential operates on one 64-byte block")
    words = list(struct.unpack("<16I", block))
    words[1] = (words[1] + (1 << 31)) & MASK_32
    words[2] = (words[2] + (1 << 31) - (1 << 28)) & MASK_32
    words[12] = (words[12] - (1 << 16)) & MASK_32
    return struct.pack("<16I", *words)


def reference_collision() -> tuple[bytes, bytes]:
    """Return the first collision pair published by Wang et al."""
    first = struct.pack("<16I", *REFERENCE_WORDS)
    return first, apply_wang_differential(first)


def is_collision(first: bytes, second: bytes) -> bool:
    """Return whether two distinct messages have the same MD4 digest."""
    return first != second and md4(first) == md4(second)


def self_test() -> None:
    """Check the MD4 primitive, attack constraints, and reference collision."""
    md4_self_test()

    first, second = reference_collision()
    if not first_round_constraints_hold(first):
        raise AssertionError("the reference message does not satisfy Wang's round-one path")
    if apply_wang_differential(first) != second:
        raise AssertionError("the reference pair does not have Wang's message differential")
    if not is_collision(first, second):
        raise AssertionError("the reference messages do not collide")
    if md4(first).hex() != REFERENCE_DIGEST:
        raise AssertionError("the reference collision has an unexpected digest")


def main() -> None:
    """Verify and display Wang et al.'s MD4 collision."""
    self_test()
    first, second = reference_collision()
    digest = md4(first).hex()

    print("Wang MD4 collision verified")
    print(f"M  = {first.hex()}")
    print(f"M' = {second.hex()}")
    print(f"MD4(M)  = {digest}")
    print(f"MD4(M') = {md4(second).hex()}")
    print(f"Different messages: {first != second}")
    print(f"Equal digests:      {is_collision(first, second)}")


if __name__ == "__main__":
    main()
