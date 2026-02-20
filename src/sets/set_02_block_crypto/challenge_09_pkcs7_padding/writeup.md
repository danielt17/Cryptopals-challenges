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

## Detailed Walkthrough
In this challenge we are asked to implement the PKCS#7 padding scheme described [here](https://datatracker.ietf.org/doc/html/rfc5652), the idea behind this padding scheme is very simple. Let's say we have a text of size m, and the block cipher block size is n where n>m, we need a padding scheme which will make our text of length m transform into length n so we can apply our block cipher. This is done in the following way: we have a block length of size n bytes and text of m bytes size (where n>m) therefore we append to the end of the text n-m bytes of the value n-m.

PKCS#7 padding extends a message to a multiple of the block size. The value of each padding byte equals the number of padding bytes added. A full block of padding is added when the input is already block-aligned.

Correct padding and unpadding are essential for block modes like CBC. The implementation should work for arbitrary block sizes, not just 16.

- Compute pad length based on block size.
- Append N bytes of value N.
- On unpad, verify padding bytes and remove them.

## Implementation Notes
Scripts: pkcs7_padding.py
Data files: none
Run: python scripts/run_challenge.py 9

## Verification
The script prints the padded output. The final length must be a multiple of the block size.

Expected output:
```text
Correct solution 

Original text: b'YELLOW SUBMARINE'. Padded text: b'YELLOW SUBMARINE\x04\x04\x04\x04' 

Unpadded text: b'YELLOW SUBMARINE'
```
