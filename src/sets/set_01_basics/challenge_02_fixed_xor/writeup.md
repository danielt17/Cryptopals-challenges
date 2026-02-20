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

## Detailed Walkthrough
Implementation of fixed [xor](https://en.wikipedia.org/wiki/Exclusive_or) between two buffers.

Fixed XOR highlights that XOR is bitwise addition modulo 2. When two equal-length buffers are XORed, each output byte is the XOR of the corresponding input bytes. XOR is reversible, so applying the same XOR twice recovers the original data.

This is a building block for many stream ciphers and one-time pads. The implementation is simple, but correctness depends on matching buffer lengths and operating on raw bytes.

- Ensure both inputs are the same length.
- XOR byte-by-byte to produce the result.
- Format the result as hex for display.

## Implementation Notes
Scripts: fixed_xor.py
Data files: none
Run: python scripts/run_challenge.py 2

## Verification
The script prints a success message when the XOR matches the challenge target.

Expected output:
```text
Success
```
