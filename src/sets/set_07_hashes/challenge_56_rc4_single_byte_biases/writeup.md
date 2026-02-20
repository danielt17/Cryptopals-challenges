# Challenge 56: RC4 single-byte biases
Set: 07 - Hashes
Cryptopals: https://cryptopals.com/sets/7/challenges/56
Run: `python scripts/run_challenge.py 56`

## Goal
Explain RC4 single-byte biases and plaintext recovery.

## Cryptographic Insight
RC4 keystream bytes are biased, especially in early positions. By collecting many ciphertexts under different keys but with a fixed plaintext structure, you can exploit these biases to recover plaintext bytes statistically.

## Method
- Collect many ciphertexts with identical plaintext prefixes.
- Use known RC4 bias tables to score candidate plaintext bytes.
- Select the most likely byte per position and reconstruct the plaintext.

## Detailed Walkthrough
## Set 8: Abstract Algebra

RC4 has biases in its early keystream bytes. With enough samples, those biases leak information about the plaintext at specific positions, enabling recovery of hidden data like cookies.

The challenge relies on collecting many ciphertexts and using statistical analysis to recover biased bytes.

- Capture many RC4-encrypted messages.
- Use bias tables for specific keystream positions.
- Recover plaintext bytes by maximum likelihood.

## Implementation Notes
Scripts: none (writeup-only challenge in this repo)
Data files: none

## Verification
No implementation is included in this repo; the writeup outlines the statistical attack.
