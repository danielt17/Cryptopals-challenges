# Challenge 53: Kelsey and Schneier's expandable messages
Set: 07 - Hashes
Cryptopals: https://cryptopals.com/sets/7/challenges/53
Run: `python scripts/run_challenge.py 53`

## Goal
Build expandable messages and use them to collide with a target hash.

## Cryptographic Insight
Expandable messages allow you to choose a prefix length later. By building a collision tree, you can match an intermediate hash of a target message and then append the target's suffix to get a full collision.

## Method
- Build a collision tree that yields messages of many lengths with the same hash.
- Find a point in the target message whose intermediate hash matches the tree root.
- Select the appropriate prefix length and append the target suffix.

## Detailed Walkthrough
Expandable messages let an attacker choose between short and long message blocks while keeping the same hash state. This enables second-preimage attacks on long messages by matching a target hash length.

The attack constructs an expandable prefix, then finds a glue block that links it to the target message.

- Build a tree of collisions with varying lengths.
- Choose lengths to match the target message length.
- Find a glue block to connect to the target hash chain.

## Implementation Notes
Scripts: expandable_messages.py
Data files: none
Run: python scripts/run_challenge.py 53

## Verification
The script prints a forged message that collides with the target hash.
