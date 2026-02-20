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

## Detailed Walkthrough
PKCS#7 padding validation checks whether the final bytes of a plaintext are a valid padding suffix. The last byte indicates the padding length, and each of the last N bytes must match that value.

Correct validation is required to avoid padding oracle vulnerabilities. The validation should reject zero padding length, out-of-range values, and inconsistent bytes.

- Read the last byte to determine N.
- Verify the last N bytes are all N.
- Remove padding only when valid.

## Implementation Notes
Scripts: pkcs7_padding_validation.py
Data files: none
Run: python scripts/run_challenge.py 15

## Verification
The script prints whether the padding is valid and demonstrates rejection for invalid input.
