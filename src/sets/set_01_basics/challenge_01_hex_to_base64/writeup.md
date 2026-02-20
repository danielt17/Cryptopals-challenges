# Challenge 01: Convert hex to base64
Set: 01 - Basics
Cryptopals: https://cryptopals.com/sets/1/challenges/1
Run: `python scripts/run_challenge.py 1`

## Goal
Convert a hex-encoded string into base64, matching the expected output.

## Cryptographic Insight
Hex and base64 are just different encodings for the same byte sequence. The task is to parse hex into raw bytes, then re-encode those bytes into base64. No cryptography yet, just careful byte handling and representation conversion.

## Method
- Parse the hex string into a byte array.
- Encode the byte array in base64.
- Compare with the expected base64 string.

## Implementation Notes
Scripts: hex_to_base64.py
Data files: none
Run: python scripts/run_challenge.py 1

## Verification
The script prints the converted base64. Validate it against the challenge's expected output.
