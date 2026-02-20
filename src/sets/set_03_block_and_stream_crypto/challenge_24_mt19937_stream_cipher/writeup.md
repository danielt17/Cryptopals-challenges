# Challenge 24: Create the MT19937 stream cipher and break it
Set: 03 - Block and stream crypto
Cryptopals: https://cryptopals.com/sets/3/challenges/24
Run: `python scripts/run_challenge.py 24`

## Goal
Build and break a stream cipher based on MT19937.

## Cryptographic Insight
Using MT19937 output as a keystream yields a stream cipher. If the seed is small or predictable, the cipher is breakable by brute forcing the seed or using known plaintext to recover the keystream.

## Method
- Generate a keystream from MT19937 and XOR with plaintext.
- Use known plaintext or brute-force a small seed space to recover the seed.
- Recreate the keystream and decrypt the ciphertext.

## Implementation Notes
Scripts: mt19937_stream_cipher.py
Data files: none
Run: python scripts/run_challenge.py 24

## Verification
The script demonstrates encryption/decryption and seed recovery.
