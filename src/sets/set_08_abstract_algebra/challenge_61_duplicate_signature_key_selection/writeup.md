# Challenge 61: Duplicate-Signature Key Selection in ECDSA (and RSA)
Link: https://toadstyle.org/cryptopals/809dccecda0e94ea588d66c12a1cf593.txt

## Goal
Forge public keys that validate a given signature in ECDSA and RSA.

## Cryptographic Insight
Given a valid signature, you can choose domain parameters to make the verification equation hold. For ECDSA, pick a new base point G' and secret d' so that the signature verifies. For RSA, choose primes p and q with smooth p-1 and q-1 and solve for a public exponent that validates the signature.

## Method
- Implement ECDSA signing and verification on a chosen curve.
- Derive a new base point G' and public key Q' that makes a fixed (r, s) verify.
- For RSA, choose p and q with smooth group orders and solve a discrete log for e'.
- Construct N' = p*q and demonstrate verification under the crafted key.

## Implementation Notes
Scripts: none (writeup-only challenge in this repo)
Data files: none

## Verification
No implementation is included; verify by crafting keys that validate a fixed signature.
