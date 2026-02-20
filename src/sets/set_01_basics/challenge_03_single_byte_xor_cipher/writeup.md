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

## Detailed Walkthrough
The solution uses a brute force approach, trying every possible single byte key, choosing the one which results in the highest English score.
In order to calculate the English score we use the [distribution](https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html)  of letters in the English language.

A single-byte XOR cipher is a stream cipher with a 1-byte key repeated for every position. The attack is to try all 256 possible keys, XOR each candidate against the ciphertext, and score the resulting plaintext for English-likeness.

The scoring uses character frequency and penalizes non-printable bytes. The key with the highest score is selected as the most likely plaintext.

- Try every key from 0 to 255.
- Score each candidate using English frequency.
- Select the plaintext with the best score.

## Implementation Notes
Scripts: single_byte_xor_cipher.py
Data files: none
Run: python scripts/run_challenge.py 3

## Verification
The script prints the best key and the recovered plaintext (the expected bacon quote).

Expected output:
```text
Decyphered text with key: 88 and score: 2.2641049 

b"Cooking MC's like a pound of bacon"
```
