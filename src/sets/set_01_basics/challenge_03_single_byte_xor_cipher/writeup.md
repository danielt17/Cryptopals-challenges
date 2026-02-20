# Challenge 03: Single-byte XOR cipher
Set: 01 - Basics
Cryptopals: https://cryptopals.com/sets/1/challenges/3
Run: `python scripts/run_challenge.py 3`

## Goal
Break a ciphertext encrypted with a single-byte XOR key.

## Cryptographic Insight
A single-byte XOR cipher is just a fixed key repeated across the plaintext. Because English text has a non-uniform distribution of characters, we can score each candidate plaintext and pick the key that yields the most English-like output.

## Method
- Try all 256 possible single-byte keys.
- XOR-decrypt the ciphertext for each key.
- Score each result using character frequency and choose the best.

## Implementation Notes
Scripts: single_byte_xor_cipher.py
Data files: none
Run: python scripts/run_challenge.py 3

## Verification
The script prints the best key and the recovered plaintext (the expected bacon quote).
