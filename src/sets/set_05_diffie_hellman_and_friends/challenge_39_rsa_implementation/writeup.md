# Challenge 39: Implement RSA
Set: 05 - Diffie-Hellman and friends
Cryptopals: https://cryptopals.com/sets/5/challenges/39
Run: `python scripts/run_challenge.py 39`

## Goal
Implement RSA key generation, encryption, and decryption.

## Cryptographic Insight
RSA relies on modular arithmetic with a composite modulus N = p*q. Encryption is m^e mod N; decryption is c^d mod N, with d the modular inverse of e mod phi(N).

## Method
- Generate two primes and compute N and phi(N).
- Choose e and compute d = e^-1 mod phi(N).
- Encrypt and decrypt messages using modular exponentiation.

## Detailed Walkthrough
This challenge implements RSA from scratch: generate primes, compute n and phi(n), choose a public exponent e, and compute the private exponent d as the modular inverse of e modulo phi(n).

Messages are converted to integers for encryption and back to bytes after decryption. Correct modular exponentiation and prime testing are required.

- Generate large primes p and q.
- Compute n, phi(n), and d.
- Encrypt and decrypt with modular exponentiation.

## Implementation Notes
Scripts: rsa_implementation.py
Data files: none
Run: python scripts/run_challenge.py 39

## Verification
The script prints RSA parameters and verifies that decryption recovers the plaintext.
