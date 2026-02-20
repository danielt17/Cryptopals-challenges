# Challenge 06: Break repeating-key XOR
Link: https://cryptopals.com/sets/1/challenges/6

## Goal
Break repeating-key XOR by recovering the key and plaintext.

## Cryptographic Insight
The key insight is that Hamming distance normalized by key size can estimate the key length. Once the key size is known, transpose the ciphertext into blocks by key position and solve each block as a single-byte XOR.

## Method
- Estimate key sizes by comparing normalized Hamming distances across blocks.
- Pick the best candidate key size(s).
- Transpose ciphertext blocks by key position and solve each as single-byte XOR.
- Reconstruct the key and decrypt the full ciphertext.

## Implementation Notes
Scripts: break_repeating_key_xor.py
Data files: 16.txt
Run: python scripts/run_challenge.py 6

## Verification
The script prints the recovered key and plaintext; the output should match the classic Vanilla Ice lyrics.
