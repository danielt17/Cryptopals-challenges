# Challenge 16: CBC bitflipping attacks
Link: https://cryptopals.com/sets/2/challenges/16

## Goal
Perform a CBC bitflipping attack to inject ';admin=true;'.

## Cryptographic Insight
In CBC decryption, each plaintext block is XORed with the previous ciphertext block. Flipping a bit in the previous ciphertext flips the corresponding plaintext bit, enabling controlled changes without knowing the key.

## Method
- Submit a user-controlled plaintext with a known structure.
- Identify the ciphertext block that precedes the target plaintext block.
- Flip bits in that ciphertext block to produce ';' and '=' in the decrypted plaintext.

## Implementation Notes
Scripts: cbc_bitflipping.py
Data files: none
Run: python scripts/run_challenge.py 16

## Verification
The script prints whether the forged admin token was accepted.
