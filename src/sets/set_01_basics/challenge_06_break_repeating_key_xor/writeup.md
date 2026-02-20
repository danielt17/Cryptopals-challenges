# Challenge 06: Break repeating-key XOR
Set: 01 - Basics
Cryptopals: https://cryptopals.com/sets/1/challenges/6
Run: `python scripts/run_challenge.py 6`

## Goal
Break repeating-key XOR by recovering the key and plaintext.

## Cryptographic Insight
The key insight is that Hamming distance normalized by key size can estimate the key length. Once the key size is known, transpose the ciphertext into blocks by key position and solve each block as a single-byte XOR.

## Method
- Estimate key sizes by comparing normalized Hamming distances across blocks.
- Pick the best candidate key size(s).
- Transpose ciphertext blocks by key position and solve each as single-byte XOR.
- Reconstruct the key and decrypt the full ciphertext.

## Detailed Walkthrough
In this challenge we break a repeating xor key also known as [Vigenere cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher). To do so we start by estimating the key length, to do so we break the ciphertext into part of the size of key length. By measuring the normalized [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance) of sequential subpart of the ciphertext, we can create a ranking of the most likely key sizes. Now we transpose the ciphertext with respect to blocks of key length size, and solve each block like a single character xor cipher as we have done before, using English text similarity ranking.

Breaking repeating-key XOR uses the fact that the key repeats with a fixed period. A good first step is to guess the key size by computing the normalized Hamming distance between consecutive blocks; the smallest normalized distances are likely key sizes.

Once the key size is known, the ciphertext is transposed into blocks where each block contains bytes XORed with the same key byte. Each block can then be solved as a single-byte XOR problem, and the recovered key bytes are combined to decrypt the message.

- Estimate key size with normalized Hamming distance.
- Transpose ciphertext into key-byte columns.
- Solve each column with the single-byte XOR scorer.

## Implementation Notes
Scripts: break_repeating_key_xor.py
Data files: 16.txt
Run: python scripts/run_challenge.py 6

## Verification
The script prints the recovered key and plaintext; the output should match the classic Vanilla Ice lyrics.

Expected output (abridged):
```text
100%|| 5/5 [00:02<00:00,  2.44it/s]

Key: b'Terminator X: Bring the noise' 

Key size: 29 

...
```
