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

## Detailed Walkthrough
Developing an algorithm to detect the use of ECB or CBC mode is simple. In ECB mode we expect the exact same block to go to the same ciphertext output, while in CBC under different IVs we expect the ciphertext blocks to be different (its 2^-64 unlikely to get a collision), developing such an algorithm is trivial from this observation.

The encryption oracle randomly chooses between ECB and CBC, with random prefix and suffix bytes. The task is to detect the mode using only the ciphertext.

The standard approach is to feed a plaintext containing repeated blocks. ECB preserves repetition, while CBC randomizes it, so repeated ciphertext blocks indicate ECB.

- Send a plaintext with many repeated blocks.
- Look for duplicate 16-byte blocks in the ciphertext.
- Classify ECB if duplicates are present; otherwise CBC.

## Implementation Notes
Scripts: ecb_cbc_detection_oracle.py
Data files: none
Run: python scripts/run_challenge.py 11

## Verification
The script runs repeated trials and reports detection accuracy.

Expected output:
```text
Experiments: 1000. Successful: 1000
```
