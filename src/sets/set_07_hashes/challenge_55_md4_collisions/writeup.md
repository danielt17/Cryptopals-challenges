# Challenge 55: MD4 collisions
Set: 07 - Hashes
Cryptopals: https://cryptopals.com/sets/7/challenges/55
Run: `python scripts/run_challenge.py 55`

## Goal
Understand and explain MD4 collision attacks.

## Cryptographic Insight
MD4 is vulnerable to differential cryptanalysis that constructs two different messages with the same hash. The attack carefully chooses message differences that cancel through the compression function.

## Method
- Define differential constraints on MD4's internal state.
- Solve for message blocks that satisfy those constraints.
- Output a pair of colliding messages.

## Detailed Walkthrough
MD4 collisions can be constructed with differential cryptanalysis by carefully controlling bit conditions across rounds. The classic attack uses message modifications to satisfy those conditions and yields a colliding pair.

This writeup describes the high-level approach even though an implementation is not included in the repo.

- Use known differential paths for MD4.
- Apply message modifications to satisfy constraints.
- Verify that the hashes collide.

## Implementation Notes
Scripts: none (writeup-only challenge in this repo)
Data files: none

## Verification
No implementation is included in this repo; this writeup documents the attack structure.
