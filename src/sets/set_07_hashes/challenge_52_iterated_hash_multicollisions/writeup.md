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

## Detailed Walkthrough
Iterated hash multicollisions are easier than expected. By finding collisions at each step, you can build 2^k distinct messages that all collide with roughly k * 2^(n/2) work for an n-bit hash.

The challenge constructs this multicollision tree and demonstrates the exponential number of colliding messages.

- Find a collision for an initial state.
- Repeat for each subsequent state.
- Combine choices to get 2^k colliding messages.

## Implementation Notes
Scripts: iterated_hash_multicollisions.py
Data files: none
Run: python scripts/run_challenge.py 52

## Verification
The script prints multiple distinct messages that share the same hash.
