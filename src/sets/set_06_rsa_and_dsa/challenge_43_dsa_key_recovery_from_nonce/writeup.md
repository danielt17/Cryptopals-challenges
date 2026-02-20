# Challenge 43: DSA key recovery from nonce
Link: https://cryptopals.com/sets/6/challenges/43

## Goal
Recover a DSA private key when a nonce is known.

## Cryptographic Insight
DSA signatures use a secret nonce k. If k is known, the private key x can be solved directly from the signature equation: x = (s*k - H(m)) * r^-1 mod q.

## Method
- Collect (r, s) and message hash H(m).
- Use the known k to solve for the private key.
- Verify by recomputing the public key.

## Implementation Notes
Scripts: dsa_key_recovery_from_nonce.py
Data files: none
Run: python scripts/run_challenge.py 43

## Verification
The script prints the recovered private key and validates it.
