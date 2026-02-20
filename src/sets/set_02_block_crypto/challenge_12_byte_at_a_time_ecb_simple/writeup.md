# Challenge 12: Byte-at-a-time ECB decryption (simple)
Set: 02 - Block crypto
Cryptopals: https://cryptopals.com/sets/2/challenges/12
Run: `python scripts/run_challenge.py 12`

## Goal
Recover an unknown suffix from an ECB oracle by decrypting one byte at a time.

## Cryptographic Insight
ECB is deterministic per block. If you can align the unknown suffix so that only one byte differs, you can build a dictionary of ciphertext blocks for each candidate byte and recover the unknown suffix iteratively.

## Method
- Discover the block size by observing ciphertext length changes.
- Confirm ECB by detecting repeated blocks.
- For each position, craft input to align the next unknown byte at block end and brute force the byte via a block dictionary.

## Implementation Notes
Scripts: byte_at_a_time_ecb_simple.py
Data files: none
Run: python scripts/run_challenge.py 12

## Verification
The script prints the recovered plaintext and intermediate iterations.
