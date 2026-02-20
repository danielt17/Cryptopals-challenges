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

## Detailed Walkthrough
MT19937 is a widely used PRNG with a 624-word internal state. Implementing it requires reproducing the seeding, twist, and tempering operations exactly.

The challenge is primarily about correctness: the output must match known test vectors. Once correct, the generator can be used as a building block for later attacks.

- Implement seeding and state initialization.
- Implement the twist transformation.
- Apply tempering to produce outputs.

## Implementation Notes
Scripts: mt19937_rng.py
Data files: none
Run: python scripts/run_challenge.py 21

## Verification
The script prints a sequence of outputs to validate the generator.
