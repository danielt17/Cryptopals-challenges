# Challenge 54: Kelsey and Kohno's Nostradamus attack
Set: 07 - Hashes
Cryptopals: https://cryptopals.com/sets/7/challenges/54
Run: `python scripts/run_challenge.py 54`

## Goal
Perform the Nostradamus preimage attack on a hash function.

## Cryptographic Insight
The Nostradamus attack precomputes a hash funnel leading to a chosen final hash. Later, you can craft a prefix that connects to the funnel and reveals a 'prediction' that hashes to the precommitted value.

## Method
- Precompute a funnel of collisions to a final hash value.
- After the event, craft a prefix that bridges into the funnel.
- Concatenate the bridge and funnel suffix to match the committed hash.

## Implementation Notes
Scripts: nostradamus_attack.py
Data files: none
Run: python scripts/run_challenge.py 54

## Verification
The script prints a prediction and a message that hashes to the committed value.
