# Challenge 51: Compression ratio side-channel attacks
Link: https://cryptopals.com/sets/7/challenges/51

## Goal
Recover secret data using a compression ratio side-channel.

## Cryptographic Insight
If attacker-controlled input is compressed alongside a secret, the compressed length leaks information. By guessing bytes and observing the length, you can recover the secret (CRIME/BREACH-style).

## Method
- Submit guesses that align with the secret and measure compressed length.
- Pick the guess that yields the shortest compression output.
- Iterate to recover the secret byte-by-byte.

## Implementation Notes
Scripts: compression_ratio_side_channel.py
Data files: none
Run: python scripts/run_challenge.py 51

## Verification
The script reports recovered secret material based on compression length differences.
