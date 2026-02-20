# Challenge 45: DSA parameter tampering
Link: https://cryptopals.com/sets/6/challenges/45

## Goal
Exploit DSA parameter tampering to forge signatures.

## Cryptographic Insight
If the generator g is set to 0 or 1, the signature verification equation becomes trivial. An attacker can create signatures that verify for any message without the private key.

## Method
- Select an unsafe g value (0 or 1 mod p).
- Generate a signature pair (r, s) that satisfies the verifier's equation.
- Verify that the signature passes without the private key.

## Implementation Notes
Scripts: dsa_parameter_tampering.py
Data files: none
Run: python scripts/run_challenge.py 45

## Verification
The script demonstrates a forged signature under tampered parameters.
