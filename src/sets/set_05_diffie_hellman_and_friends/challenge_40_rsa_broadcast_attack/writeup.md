# Challenge 40: RSA broadcast attack (e=3)
Set: 05 - Diffie-Hellman and friends
Cryptopals: https://cryptopals.com/sets/5/challenges/40
Run: `python scripts/run_challenge.py 40`

## Goal
Recover plaintext from RSA broadcast with e=3 using CRT.

## Cryptographic Insight
If the same plaintext is sent to multiple recipients with the same small exponent e and no padding, the attacker can use the Chinese Remainder Theorem to reconstruct m^e and take the integer root.

## Method
- Collect at least three ciphertexts of the same message under different moduli.
- Use CRT to combine them into a single value equal to m^3.
- Compute the integer cube root to recover m.

## Detailed Walkthrough
## Set 6: RSA and DSA

The RSA broadcast attack shows that RSA with e=3 is vulnerable when the same plaintext is sent to multiple recipients without padding. With three ciphertexts under different moduli, the Chinese Remainder Theorem recovers m^3.

Taking the integer cube root yields the original message.

- Collect three ciphertexts of the same message.
- Use CRT to combine them into m^3.
- Compute the integer cube root to recover m.

## Implementation Notes
Scripts: rsa_broadcast_attack.py
Data files: none
Run: python scripts/run_challenge.py 40

## Verification
The script prints the recovered plaintext and confirms correctness.
