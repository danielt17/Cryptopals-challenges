# Challenge 04: Detect single-character XOR
Set: 01 - Basics
Cryptopals: https://cryptopals.com/sets/1/challenges/4
Run: `python scripts/run_challenge.py 4`

## Goal
Detect which line in a file is encrypted with single-byte XOR and decrypt it.

## Cryptographic Insight
This is the same attack as Challenge 3, but applied to many candidate ciphertexts. The most English-like output across all lines indicates the correct line and key.

## Method
- Read each hex-encoded line from the input file.
- Run the single-byte XOR brute force and scoring for each line.
- Select the highest-scoring result and report the plaintext.

## Detailed Walkthrough
Using the same approach used in [challenge 3](#challenge-3), where now we use the English score to find the most likely sequence to be encrypted by a single byte xor cipher, therefore both detecting and decrypting using the English score metric.

This challenge extends the single-byte XOR attack by scanning many candidate ciphertexts. Each line is tested with the same brute force method, and the best-scoring result across all lines is chosen.

The trick is to compute comparable scores for every line and keep the global maximum. The correct line stands out because its decrypted text reads like English.

- Iterate over every candidate line.
- Run the single-byte XOR solver per line.
- Pick the best overall score and output that plaintext.

## Implementation Notes
Scripts: detect_single_character_xor.py
Data files: 14.txt
Run: python scripts/run_challenge.py 4

## Verification
The script prints the best candidate line, key, and decrypted text.

Expected output:
```text
Decyphered text with key: 53 and score: 2.0881317999999998 Cur line: 170 

b'Now that the party is jumping\n'
```
