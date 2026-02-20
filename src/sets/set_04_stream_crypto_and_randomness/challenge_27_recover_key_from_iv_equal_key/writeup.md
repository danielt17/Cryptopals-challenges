# Challenge 27: Recover the key from CBC with IV=Key
Set: 04 - Stream crypto and randomness
Cryptopals: https://cryptopals.com/sets/4/challenges/27
Run: `python scripts/run_challenge.py 27`

## Goal
Recover the AES key when CBC uses IV=Key.

## Cryptographic Insight
If the IV equals the key, CBC decryption leaks the key via crafted ciphertexts. By forcing decryption of blocks that reveal P1 and P3, you can compute the key as P1 XOR P3.

## Method
- Construct a ciphertext with blocks C1, all-zero block, C1.
- Decrypt to obtain plaintext blocks P1, P2, P3.
- Compute key = P1 XOR P3.

## Implementation Notes
Scripts: recover_key_from_iv_equal_key.py
Data files: none
Run: python scripts/run_challenge.py 27

## Verification
The script prints the recovered key and verifies it against encryption/decryption.
