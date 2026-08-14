"""A small, dependency-free implementation of the MD4 hash function.

This module follows RFC 1320 and supports arbitrary byte strings, including
messages that span multiple 512-bit blocks.

MD4 is obsolete and must not be used for security-sensitive applications.
"""

from __future__ import annotations

from collections.abc import Sequence
import struct


MASK_32 = 0xFFFFFFFF
INITIAL_STATE = (0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476)  # (a,b,c,d)

ROUND_ORDERS = (
    tuple(range(16)),
    (0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15),
    (0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15),
)
ROUND_SHIFTS = ((3, 7, 11, 19), (3, 5, 9, 13), (3, 9, 11, 15))
ROUND_CONSTANTS = (0, 0x5A827999, 0x6ED9EBA1)
TARGET_ORDER = (0, 3, 2, 1)  # a, d, c, b


def left_rotate(value: int, amount: int) -> int:
    """Rotate a 32-bit integer left."""
    value &= MASK_32
    return ((value << amount) | (value >> (32 - amount))) & MASK_32


def right_rotate(value: int, amount: int) -> int:
    """Rotate a 32-bit integer right."""
    value &= MASK_32
    return ((value >> amount) | (value << (32 - amount))) & MASK_32


def md4_f(x: int, y: int, z: int) -> int:
    """Return MD4's round-one Boolean function."""
    return (x & y) | (~x & z)


def _g(x: int, y: int, z: int) -> int:
    return (x & y) | (x & z) | (y & z)


def _h(x: int, y: int, z: int) -> int:
    return x ^ y ^ z


ROUND_FUNCTIONS = (md4_f, _g, _h)


def step_inputs(state: Sequence[int], target: int) -> tuple[int, int, int]:
    """Return the Boolean-function inputs for an a/d/c/b MD4 step."""
    if target == 0:  # a <- op(a, b, c, d)
        return state[1], state[2], state[3]
    if target == 3:  # d <- op(d, a, b, c)
        return state[0], state[1], state[2]
    if target == 2:  # c <- op(c, d, a, b)
        return state[3], state[0], state[1]
    return state[2], state[3], state[0]  # b <- op(b, c, d, a)


def _compress(words: Sequence[int], state: Sequence[int] = INITIAL_STATE) -> tuple[int, ...]:
    """Run the MD4 compression function over one 16-word block."""
    if len(words) != 16:
        raise ValueError("an MD4 compression block must contain exactly 16 words")
    if len(state) != 4:
        raise ValueError("an MD4 state must contain exactly four words")

    working = [word & MASK_32 for word in state]  # keep 32 lowest bits
    original = tuple(working)
    for round_number in range(3):
        function = ROUND_FUNCTIONS[round_number]
        constant = ROUND_CONSTANTS[round_number]
        for step, word_index in enumerate(ROUND_ORDERS[round_number]):
            target = TARGET_ORDER[step % 4]
            x, y, z = step_inputs(working, target)
            value = working[target] + function(x, y, z) + words[word_index] + constant
            working[target] = left_rotate(value, ROUND_SHIFTS[round_number][step % 4])

    return tuple((value + original[index]) & MASK_32 for index, value in enumerate(working))


def md4(message: bytes) -> bytes:
    """Return the RFC 1320 MD4 digest of *message*."""
    bit_length = len(message) * 8
    padding_length = (56 - (len(message) + 1) % 64) % 64  # up to 448 mod 512
    padded = message + b"\x80" + bytes(padding_length) + struct.pack("<Q", bit_length)

    state: tuple[int, ...] = INITIAL_STATE
    for offset in range(0, len(padded), 64):
        words = struct.unpack("<16I", padded[offset : offset + 64])
        state = _compress(words, state)
    return struct.pack("<4I", *state)


def self_test() -> None:
    """Validate the implementation against the RFC 1320 test suite."""
    vectors = {
        b"": "31d6cfe0d16ae931b73c59d7e0c089c0",
        b"a": "bde52cb31de33e46245e05fbdbd6fb24",
        b"abc": "a448017aaf21d8525fc10ae87aa6729d",
        b"message digest": "d9130a8164549fe818874806e1c7014b",
        b"abcdefghijklmnopqrstuvwxyz": "d79e1c308aa5bbcdeea8ed63df412da9",
        b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789": (
            "043f8582f241db351ce627e153e7f0e4"
        ),
        b"12345678901234567890123456789012345678901234567890123456789012345678901234567890": (
            "e33b4ddc9c38f2199c3e7b164fcc0536"
        ),
    }
    for message, expected in vectors.items():
        actual = md4(message).hex()
        if actual != expected:
            raise AssertionError(f"MD4 test vector failed: {actual} != {expected}")


def main() -> None:
    """Run the MD4 self-test."""
    self_test()
    print("MD4 RFC 1320 test vectors passed")


if __name__ == "__main__":
    main()
