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

## Detailed Walkthrough
Diffie-Hellman establishes a shared secret over an insecure channel. Each party computes g^a mod p and g^b mod p, then derives a shared secret as (g^b)^a mod p.

The challenge focuses on correct modular exponentiation and the matching of shared secrets.

- Generate private exponents.
- Compute public values and exchange them.
- Derive the shared secret and hash it for a key.

## Implementation Notes
Scripts: diffie_hellman.py
Data files: none
Run: python scripts/run_challenge.py 33

## Verification
The script prints matching shared secrets for both parties.
