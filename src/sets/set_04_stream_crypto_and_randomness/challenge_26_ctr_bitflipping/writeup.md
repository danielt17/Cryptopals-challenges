# Challenge 26: CTR bitflipping
Set: 04 - Stream crypto and randomness
Cryptopals: https://cryptopals.com/sets/4/challenges/26
Run: `python scripts/run_challenge.py 26`

## Goal
Perform a CTR bitflipping attack to inject data into plaintext.

## Cryptographic Insight
CTR decryption XORs ciphertext with keystream. Flipping a ciphertext bit flips the corresponding plaintext bit, allowing controlled modifications without knowing the key.

## Method
- Submit a chosen plaintext with sanitized characters.
- Locate the ciphertext positions that map to the target plaintext bytes.
- Flip the needed bits to produce the desired substring on decryption.

## Detailed Walkthrough
CTR bitflipping is the stream-cipher analog of CBC bitflipping. Because ciphertext is plaintext XOR keystream, flipping a bit in the ciphertext flips the same bit in the plaintext.

This makes CTR malleable. The attack injects forbidden substrings by flipping bits at the right offsets.

- Identify where the target text should appear.
- XOR the ciphertext bytes to flip into the desired plaintext bytes.
- Verify the decrypted plaintext contains the injected field.

## Implementation Notes
Scripts: ctr_bitflipping.py
Data files: none
Run: python scripts/run_challenge.py 26

## Verification
The script reports whether the injected admin token appears in the decrypted plaintext.
