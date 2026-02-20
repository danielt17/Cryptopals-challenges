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

## Implementation Notes
Scripts: detect_aes_ecb_mode.py
Data files: 18.txt
Run: python scripts/run_challenge.py 8

## Verification
The script prints the ciphertext line with the strongest ECB signature.
