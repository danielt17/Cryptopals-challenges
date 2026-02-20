# Challenge 33: Implement Diffie-Hellman
Set: 05 - Diffie-Hellman and friends
Cryptopals: https://cryptopals.com/sets/5/challenges/33
Run: `python scripts/run_challenge.py 33`

## Goal
Implement basic Diffie-Hellman key exchange.

## Cryptographic Insight
Diffie-Hellman lets two parties agree on a shared secret via modular exponentiation: each side computes g^ab mod p from their own secret exponent and the other's public value.

## Method
- Generate a prime modulus p and generator g.
- Each party picks a secret exponent and publishes g^secret mod p.
- Each side computes the shared secret using the peer's public value.

## Implementation Notes
Scripts: diffie_hellman.py
Data files: none
Run: python scripts/run_challenge.py 33

## Verification
The script prints matching shared secrets for both parties.
