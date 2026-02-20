# Challenge 10: Implement CBC mode
Set: 02 - Block crypto
Cryptopals: https://cryptopals.com/sets/2/challenges/10
Run: `python scripts/run_challenge.py 10`

## Goal
Implement AES-CBC encryption and decryption using AES-ECB as the block primitive.

## Cryptographic Insight
CBC chains blocks by XORing each plaintext block with the previous ciphertext block (or IV) before encryption. Decryption reverses this by decrypting then XORing with the previous ciphertext block.

## Method
- Pad the plaintext to the AES block size.
- For each block: XOR with previous ciphertext (or IV) and encrypt with AES-ECB.
- For decryption: decrypt each block and XOR with previous ciphertext (or IV).

## Implementation Notes
Scripts: cbc_mode.py
Data files: 22.txt
Run: python scripts/run_challenge.py 10

## Verification
The script decrypts the provided ciphertext and verifies the encrypt-decrypt round trip.
