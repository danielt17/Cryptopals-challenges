# Challenge 07: AES in ECB mode
Set: 01 - Basics
Cryptopals: https://cryptopals.com/sets/1/challenges/7
Run: `python scripts/run_challenge.py 7`

## Goal
Decrypt an AES-ECB ciphertext with a known key.

## Cryptographic Insight
ECB mode encrypts each block independently. With a known key, decryption is straightforward block-by-block AES without any chaining or IV.

## Method
- Decode the base64 ciphertext from the input file.
- Decrypt with AES-128-ECB using the provided key.
- Strip the trailing padding and display the plaintext.

## Implementation Notes
Scripts: aes_ecb_mode.py
Data files: 17.txt
Run: python scripts/run_challenge.py 7

## Verification
The script prints the decrypted text and checks a simple encryption/decryption round-trip.
