# Challenge 08: Detect AES in ECB mode
Set: 01 - Basics
Cryptopals: https://cryptopals.com/sets/1/challenges/8
Run: `python scripts/run_challenge.py 8`

## Goal
Detect which ciphertext in a set is likely encrypted with AES-ECB.

## Cryptographic Insight
ECB mode leaks structure: identical plaintext blocks yield identical ciphertext blocks. Repeated 16-byte blocks in the ciphertext are strong evidence of ECB.

## Method
- Read the candidate ciphertext from the input file.
- Split into 16-byte blocks and count repeats.
- Select the ciphertext with the highest repetition score.

## Detailed Walkthrough
In order to detect which file has been encrypted by AES in ECB mode, we need to search for repeating 16 bytes blocks, as its very unlikely (2^-64 unlikely) that a repeating block will happen for any other mode operation of AES.

ECB mode is deterministic: identical plaintext blocks produce identical ciphertext blocks. This property leaks patterns and makes ECB easy to detect.

The detection method splits the ciphertext into 16-byte blocks and counts duplicates. The ciphertext with the highest number of repeated blocks is likely ECB.

- Split ciphertext into 16-byte blocks.
- Count duplicate blocks.
- Flag the ciphertext with the most repeats.

## Implementation Notes
Scripts: detect_aes_ecb_mode.py
Data files: 18.txt
Run: python scripts/run_challenge.py 8

## Verification
The script prints the ciphertext line with the strongest ECB signature.

Expected output:
```text
AES ECB encrypted file: 165
```
