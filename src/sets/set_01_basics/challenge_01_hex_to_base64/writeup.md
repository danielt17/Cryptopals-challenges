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

## Detailed Walkthrough
Converting [Hex](https://en.wikipedia.org/wiki/Hexadecimal) to [base64](https://en.wikipedia.org/wiki/Base64), by first transforming the hex string to a bytes object, afterward transforming it into base64.

This challenge is about encodings, not encryption. Hex encodes each byte as two hexadecimal digits, while base64 groups bytes into 24-bit chunks and maps them to four characters from a fixed alphabet. The important part is to treat the input as raw bytes, not as Unicode text.

The safe pipeline is to parse the hex string into bytes, then base64-encode those bytes. Any string slicing should only happen on the final base64 text, never on the intermediate byte data.

- Parse two hex characters into one byte.
- Encode bytes to base64 using standard padding rules.
- Compare the output with the expected base64 string.

## Implementation Notes
Scripts: hex_to_base64.py
Data files: none
Run: python scripts/run_challenge.py 1

## Verification
The script prints the converted base64. Validate it against the challenge's expected output.

Expected output:
```text
solved
```
