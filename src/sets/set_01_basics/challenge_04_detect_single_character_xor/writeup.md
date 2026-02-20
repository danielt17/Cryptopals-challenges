# Challenge 04: Detect single-character XOR
Link: https://cryptopals.com/sets/1/challenges/4

## Goal
Detect which line in a file is encrypted with single-byte XOR and decrypt it.

## Cryptographic Insight
This is the same attack as Challenge 3, but applied to many candidate ciphertexts. The most English-like output across all lines indicates the correct line and key.

## Method
- Read each hex-encoded line from the input file.
- Run the single-byte XOR brute force and scoring for each line.
- Select the highest-scoring result and report the plaintext.

## Implementation Notes
Scripts: detect_single_character_xor.py
Data files: 14.txt
Run: python scripts/run_challenge.py 4

## Verification
The script prints the best candidate line, key, and decrypted text.
