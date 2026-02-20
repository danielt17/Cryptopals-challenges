# Challenge 05: Implement repeating-key XOR
Set: 01 - Basics
Cryptopals: https://cryptopals.com/sets/1/challenges/5
Run: `python scripts/run_challenge.py 5`

## Goal
Implement repeating-key XOR encryption.

## Cryptographic Insight
Repeating-key XOR (Vigenere) applies the key cyclically across the plaintext. It is the basic model for many stream ciphers where a keystream is XORed with plaintext, but the keystream here is just the key repeated.

## Method
- Take a plaintext and key as byte sequences.
- Repeat the key to match the plaintext length.
- XOR each plaintext byte with the corresponding key byte.

## Implementation Notes
Scripts: repeating_key_xor.py
Data files: none
Run: python scripts/run_challenge.py 5

## Verification
The script prints a success message when the produced ciphertext matches the expected value.
