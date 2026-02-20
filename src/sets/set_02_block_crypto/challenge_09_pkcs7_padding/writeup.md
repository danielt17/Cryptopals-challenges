# Challenge 09: Implement PKCS#7 padding
Set: 02 - Block crypto
Cryptopals: https://cryptopals.com/sets/2/challenges/9
Run: `python scripts/run_challenge.py 9`

## Goal
Implement PKCS#7 padding for arbitrary block sizes.

## Cryptographic Insight
Block ciphers require input lengths aligned to the block size. PKCS#7 pads by appending N bytes of value N, where N is the number of padding bytes required. This makes padding unambiguous and reversible.

## Method
- Compute the number of padding bytes needed to reach a multiple of the block size.
- Append that many bytes, each with value equal to the pad length.
- Return the padded result.

## Implementation Notes
Scripts: pkcs7_padding.py
Data files: none
Run: python scripts/run_challenge.py 9

## Verification
The script prints the padded output. The final length must be a multiple of the block size.
