# Challenge 15: PKCS#7 padding validation
Set: 02 - Block crypto
Cryptopals: https://cryptopals.com/sets/2/challenges/15
Run: `python scripts/run_challenge.py 15`

## Goal
Validate PKCS#7 padding and reject invalid padding.

## Cryptographic Insight
PKCS#7 padding is valid when the last byte value N appears exactly N times at the end. Incorrect padding should be rejected to prevent padding oracle vulnerabilities.

## Method
- Read the last byte to get the expected padding length.
- Check that the last N bytes all equal the pad length.
- If valid, strip the padding; otherwise reject.

## Implementation Notes
Scripts: pkcs7_padding_validation.py
Data files: none
Run: python scripts/run_challenge.py 15

## Verification
The script prints whether the padding is valid and demonstrates rejection for invalid input.
