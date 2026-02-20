# Challenge 51: Compression ratio side-channel attacks
Set: 07 - Hashes
Cryptopals: https://cryptopals.com/sets/7/challenges/51
Run: `python scripts/run_challenge.py 51`

## Goal
Recover secret data using a compression ratio side-channel.

## Cryptographic Insight
If attacker-controlled input is compressed alongside a secret, the compressed length leaks information. By guessing bytes and observing the length, you can recover the secret (CRIME/BREACH-style).

## Method
- Submit guesses that align with the secret and measure compressed length.
- Pick the guess that yields the shortest compression output.
- Iterate to recover the secret byte-by-byte.

## Detailed Walkthrough
Compression ratio side-channel attacks (CRIME) exploit the fact that compression reveals information about repeated substrings. If a secret is included in a compressed request, you can guess the secret by observing which guesses compress best.

The attack iteratively guesses the secret one byte at a time by sending crafted requests and measuring ciphertext length after compression and encryption.

- Build requests that place a guess next to the secret.
- Compare compressed lengths to find the best match.
- Repeat to recover the secret.

## Implementation Notes
Scripts: compression_ratio_side_channel.py
Data files: none
Run: python scripts/run_challenge.py 51

## Verification
The script reports recovered secret material based on compression length differences.
