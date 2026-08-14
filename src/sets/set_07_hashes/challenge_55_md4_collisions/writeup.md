# Challenge 55: MD4 collisions
Set: 07 - Hashes
Cryptopals: https://cryptopals.com/sets/7/challenges/55
Run: `python scripts/run_challenge.py 55`

## Goal
Demonstrate the practical collision attack on MD4 described by Wang et al.

## Cryptographic Insight
MD4 processes a 512-bit block as sixteen little-endian 32-bit words. Wang's
differential changes only three of those words, using modular arithmetic:

```text
m'[1]  = m[1]  + 2^31
m'[2]  = m[2]  + 2^31 - 2^28
m'[12] = m[12] - 2^16
```

These differences do not collide for an arbitrary block. The intermediate MD4
state must follow a carefully selected differential path. During round one,
each message word is consumed exactly once and in order. That makes its bit
conditions directly enforceable: compute a state word, correct its constrained
bits, then invert the rotation, addition, and Boolean function to recover the
corresponding message word.

## Method
- Implement MD4 in the reusable `md4.py` module, including padding and
  multi-block input from RFC 1320.
- Encode the first-round sufficient conditions from Table 6 of Wang et al.
- Implement single-step message modification for arbitrary 64-byte blocks.
- Apply Wang's three-word differential to construct the sister block.
- Reproduce the first published collision pair and prove that the two distinct
  messages have the same standard, padded MD4 digest.

The normal challenge run uses the published pair so it is deterministic and
fast. `massage_first_round()` exposes the important message-modification stage
for experimentation; the paper's additional multi-step modifications are what
raise a fresh candidate's success probability from roughly 2^-25 to between
2^-6 and 2^-2.

## Verification
The MD4 module checks all seven RFC 1320 test vectors. The collision script
validates every encoded first-round constraint, confirms the exact three-word
differential, and rejects equal-message false positives before reporting a
collision.

Expected digest:

```text
4d7e6a1defa93d2dde05b45d864c429b
```

## References
- [Cryptopals challenge 55](https://cryptopals.com/sets/7/challenges/55)
- [Wang et al., Cryptanalysis of the Hash Functions MD4 and RIPEMD](https://doi.org/10.1007/11426639_1)
- [RFC 1320: The MD4 Message-Digest Algorithm](https://www.rfc-editor.org/rfc/rfc1320)
