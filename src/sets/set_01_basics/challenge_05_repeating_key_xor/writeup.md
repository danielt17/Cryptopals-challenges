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

## Detailed Walkthrough
Implemenating a simple repeating-key [XOR cipher](https://en.wikipedia.org/wiki/XOR_cipher), the implementation is very straight forward using a cyclic loop over the key characters.

Repeating-key XOR, also known as a Vigenere-style XOR, uses a short key repeated across the plaintext. Each plaintext byte is XORed with the corresponding key byte in a cyclic fashion.

The attack is not required here, only correct encryption. The key point is to repeat the key exactly and to keep all operations on bytes rather than strings.

- Iterate over plaintext bytes.
- XOR each byte with the repeating key byte.
- Emit the resulting ciphertext as hex.

## Implementation Notes
Scripts: repeating_key_xor.py
Data files: none
Run: python scripts/run_challenge.py 5

## Verification
The script prints a success message when the produced ciphertext matches the expected value.

Expected output:
```text
sucess
```
