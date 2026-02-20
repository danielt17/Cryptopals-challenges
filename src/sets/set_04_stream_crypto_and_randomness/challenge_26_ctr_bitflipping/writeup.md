# Challenge 26: CTR bitflipping
Link: https://cryptopals.com/sets/4/challenges/26

## Goal
Perform a CTR bitflipping attack to inject data into plaintext.

## Cryptographic Insight
CTR decryption XORs ciphertext with keystream. Flipping a ciphertext bit flips the corresponding plaintext bit, allowing controlled modifications without knowing the key.

## Method
- Submit a chosen plaintext with sanitized characters.
- Locate the ciphertext positions that map to the target plaintext bytes.
- Flip the needed bits to produce the desired substring on decryption.

## Implementation Notes
Scripts: ctr_bitflipping.py
Data files: none
Run: python scripts/run_challenge.py 26

## Verification
The script reports whether the injected admin token appears in the decrypted plaintext.
