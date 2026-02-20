# Challenge 19: Break fixed-nonce CTR mode using substitutions
Set: 03 - Block and stream crypto
Cryptopals: https://cryptopals.com/sets/3/challenges/19
Run: `python scripts/run_challenge.py 19`

## Goal
Break fixed-nonce CTR mode using substitutions.

## Cryptographic Insight
Reusing a nonce in CTR reuses the keystream, making the ciphertexts equivalent to repeating-key XOR. With enough ciphertexts, you can infer the keystream by exploiting English plaintext statistics.

## Method
- Collect multiple ciphertexts encrypted with the same nonce.
- Treat each position across ciphertexts as a single-byte XOR problem.
- Recover the keystream and decrypt all messages.

## Detailed Walkthrough
Fixed-nonce CTR means every message is encrypted with the same keystream. This reduces the problem to breaking a repeating-key XOR across many ciphertexts.

The attack aligns ciphertext bytes by position and uses substitution or scoring to recover the keystream and plaintexts.

- Align ciphertexts by index position.
- Use English scoring to guess keystream bytes.
- Recover plaintexts by XORing with the keystream.

## Implementation Notes
Scripts: break_fixed_nonce_ctr.py
Data files: 33.txt
Run: python scripts/run_challenge.py 19

## Verification
The script reconstructs the plaintexts by deriving a shared keystream.
