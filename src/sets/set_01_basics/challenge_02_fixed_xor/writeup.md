# Challenge 02: Fixed XOR
Set: 01 - Basics
Cryptopals: https://cryptopals.com/sets/1/challenges/2
Run: `python scripts/run_challenge.py 2`

## Goal
XOR two equal-length buffers and output the resulting bytes.

## Cryptographic Insight
XOR is a linear, bitwise operation. When applied to equal-length buffers, each output byte is the XOR of the corresponding input bytes. This is the core primitive behind many stream ciphers and several attacks in later challenges.

## Method
- Convert both inputs into bytes of equal length.
- XOR each byte pair and build the output buffer.
- Display the resulting hex string.

## Implementation Notes
Scripts: fixed_xor.py
Data files: none
Run: python scripts/run_challenge.py 2

## Verification
The script prints a success message when the XOR matches the challenge target.
