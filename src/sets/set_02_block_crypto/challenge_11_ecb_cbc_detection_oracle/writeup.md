# Challenge 11: An ECB/CBC detection oracle
Set: 02 - Block crypto
Cryptopals: https://cryptopals.com/sets/2/challenges/11
Run: `python scripts/run_challenge.py 11`

## Goal
Build an oracle that encrypts under ECB or CBC and detect the mode.

## Cryptographic Insight
ECB mode leaks identical blocks, while CBC randomizes identical blocks with the IV and chaining. By feeding repeated plaintext blocks, you can detect ECB by repeated ciphertext blocks.

## Method
- Construct an input with many repeated blocks.
- Encrypt with the unknown mode (ECB or CBC).
- Look for repeated ciphertext blocks to identify ECB; otherwise infer CBC.

## Implementation Notes
Scripts: ecb_cbc_detection_oracle.py
Data files: none
Run: python scripts/run_challenge.py 11

## Verification
The script runs repeated trials and reports detection accuracy.
