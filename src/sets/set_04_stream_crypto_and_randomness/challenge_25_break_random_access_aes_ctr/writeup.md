# Challenge 25: Break random-access read/write AES CTR
Set: 04 - Stream crypto and randomness
Cryptopals: https://cryptopals.com/sets/4/challenges/25
Run: `python scripts/run_challenge.py 25`

## Goal
Recover plaintext from an AES-CTR ciphertext given a random-access edit oracle.

## Cryptographic Insight
CTR mode exposes a keystream. If an oracle allows editing ciphertext by re-encrypting modified plaintext, you can ask it to encrypt zeros and directly recover the keystream, then XOR to get the plaintext.

## Method
- Use the edit function to replace the plaintext with all-zero bytes.
- Capture the resulting ciphertext, which equals the keystream.
- XOR the original ciphertext with the keystream to recover plaintext.

## Implementation Notes
Scripts: break_random_access_aes_ctr.py
Data files: 41.txt
Run: python scripts/run_challenge.py 25

## Verification
The script prints the recovered plaintext and confirms the attack.
