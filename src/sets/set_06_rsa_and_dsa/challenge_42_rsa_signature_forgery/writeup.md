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

## Detailed Walkthrough
RSA signature forgery with e=3 exploits lax PKCS#1 v1.5 verification. If the verifier only checks that the signature block starts with a valid ASN.1 prefix, you can forge a signature by taking an integer cube root of a crafted block.

The forged block contains the required prefix and hash, followed by junk that is ignored by a weak verifier.

- Build a padded block with the correct hash prefix.
- Compute an integer cube root as the signature.
- Verify that the lax parser accepts the forged signature.

## Implementation Notes
Scripts: rsa_signature_forgery.py
Data files: none
Run: python scripts/run_challenge.py 42

## Verification
The script prints a forged signature that passes the verifier.
