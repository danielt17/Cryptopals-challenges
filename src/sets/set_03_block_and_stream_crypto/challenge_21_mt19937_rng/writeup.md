# Challenge 21: Implement the MT19937 Mersenne Twister RNG
Set: 03 - Block and stream crypto
Cryptopals: https://cryptopals.com/sets/3/challenges/21
Run: `python scripts/run_challenge.py 21`

## Goal
Implement the MT19937 Mersenne Twister PRNG.

## Cryptographic Insight
MT19937 is a linear PRNG with a large internal state (624 32-bit values). Implementing it correctly is a prerequisite for later cloning and attacks.

## Method
- Implement the MT19937 state initialization.
- Generate outputs with the twist and temper functions.
- Verify output against known vectors or internal consistency checks.

## Implementation Notes
Scripts: mt19937_rng.py
Data files: none
Run: python scripts/run_challenge.py 21

## Verification
The script prints a sequence of outputs to validate the generator.
