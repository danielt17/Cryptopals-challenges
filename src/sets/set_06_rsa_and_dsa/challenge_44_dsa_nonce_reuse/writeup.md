# Challenge 44: DSA nonce reuse
Set: 06 - RSA and DSA
Cryptopals: https://cryptopals.com/sets/6/challenges/44
Run: `python scripts/run_challenge.py 44`

## Goal
Recover a DSA private key from repeated nonces.

## Cryptographic Insight
If two signatures reuse the same nonce k, the difference between the signatures reveals k. Once k is known, the private key is solvable from the signature equation.

## Method
- Identify two signatures with identical r values (same k).
- Solve for k using the two signature equations.
- Recover the private key and verify it.

## Implementation Notes
Scripts: dsa_nonce_reuse.py
Data files: 64.txt
Run: python scripts/run_challenge.py 44

## Verification
The script prints the recovered key and checks it against the expected public key.
