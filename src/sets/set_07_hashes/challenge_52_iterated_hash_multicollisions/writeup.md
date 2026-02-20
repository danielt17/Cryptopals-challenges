# Challenge 52: Iterated hash function multicollisions
Set: 07 - Hashes
Cryptopals: https://cryptopals.com/sets/7/challenges/52
Run: `python scripts/run_challenge.py 52`

## Goal
Construct multicollisions for an iterated hash function.

## Cryptographic Insight
Merkle-Damgard hashes allow 2^k collisions with only O(k) work by chaining collisions at each block. This shows that multicollisions are much cheaper than naive expectations.

## Method
- Find a collision for the first block to create two states.
- For each subsequent block, find collisions for each state pair.
- Combine choices to produce 2^k colliding messages.

## Implementation Notes
Scripts: iterated_hash_multicollisions.py
Data files: none
Run: python scripts/run_challenge.py 52

## Verification
The script prints multiple distinct messages that share the same hash.
