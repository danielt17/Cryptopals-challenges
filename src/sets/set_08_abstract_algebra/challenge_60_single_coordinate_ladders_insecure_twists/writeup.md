# Challenge 60: Single-Coordinate Ladders and Insecure Twists
Set: 08 - Abstract Algebra
Cryptopals: https://toadstyle.org/cryptopals/c53b90a3e9e753ddad56edbbd33838aa.txt
Run: `python scripts/run_challenge.py 60`

## Goal
Implement a Montgomery ladder and exploit insecure twists.

## Cryptographic Insight
Montgomery curves allow a fast single-coordinate ladder. However, points on the quadratic twist can still be used for invalid-curve attacks if the twist has small subgroups. The ladder accepts a u coordinate even if it is not on the original curve, enabling twist-based leakage.

## Method
- Implement the Montgomery ladder to compute the u-coordinate of k*P.
- Map between the Weierstrass and Montgomery forms using the provided isomorphism.
- Compute the twist order and find small-order points on the twist.
- Use these points to recover key bits and apply Pollard's kangaroo for the remainder.

## Implementation Notes
Scripts: none (writeup-only challenge in this repo)
Data files: none

## Verification
Verify ladder correctness with the base point and test the twist attack on sample inputs.
