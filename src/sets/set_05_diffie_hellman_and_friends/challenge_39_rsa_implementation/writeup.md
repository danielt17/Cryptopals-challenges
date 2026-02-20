# Challenge 39: Implement RSA
Link: https://cryptopals.com/sets/5/challenges/39

## Goal
Implement RSA key generation, encryption, and decryption.

## Cryptographic Insight
RSA relies on modular arithmetic with a composite modulus N = p*q. Encryption is m^e mod N; decryption is c^d mod N, with d the modular inverse of e mod phi(N).

## Method
- Generate two primes and compute N and phi(N).
- Choose e and compute d = e^-1 mod phi(N).
- Encrypt and decrypt messages using modular exponentiation.

## Implementation Notes
Scripts: rsa_implementation.py
Data files: none
Run: python scripts/run_challenge.py 39

## Verification
The script prints RSA parameters and verifies that decryption recovers the plaintext.
