# Challenge 42: Bleichenbacher's e=3 RSA signature forgery
Set: 06 - RSA and DSA
Cryptopals: https://cryptopals.com/sets/6/challenges/42
Run: `python scripts/run_challenge.py 42`

## Goal
Forge an RSA signature when the verifier is too lenient.

## Cryptographic Insight
With e=3 and lax ASN.1/padding checks, an attacker can craft a signature whose cube begins with a valid padding prefix. The verifier only checks the prefix and accepts the forgery.

## Method
- Construct a padded block containing the ASN.1 hash prefix and digest.
- Take an integer cube root to find a signature candidate.
- Verify that the cube of the candidate matches the required prefix.

## Implementation Notes
Scripts: rsa_signature_forgery.py
Data files: none
Run: python scripts/run_challenge.py 42

## Verification
The script prints a forged signature that passes the verifier.
