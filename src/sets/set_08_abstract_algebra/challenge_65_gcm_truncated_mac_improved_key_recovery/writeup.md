# Challenge 65: Truncated-MAC GCM Revisited: Improving the Key-Recovery Attack
Set: 08 - Abstract Algebra
Cryptopals: https://toadstyle.org/cryptopals/a1a2e7311ec5f2535ec46eaebd4588f0.txt
Run: `python scripts/run_challenge.py 65`

## Goal
Improve the truncated GCM attack using ciphertext length extension.

## Cryptographic Insight
If the last ciphertext block is partial, you can tweak the length block to gain additional degrees of freedom. This turns the homogeneous system T*d = 0 into T*d = t, letting you force more rows to zero and accelerate key recovery.

## Method
- Detect when the last ciphertext block is incomplete.
- Adjust the length block to introduce a controlled offset.
- Solve the linear system for a particular solution and add null-space vectors.
- Use the improved degrees of freedom to forge more efficiently.

## Detailed Walkthrough
This challenge improves the truncated-tag GCM attack by using more efficient equations and query strategies. The goal is to reduce the number of required queries while still recovering the GHASH key.

It demonstrates how structural weaknesses become exploitable at scale when tags are truncated.

- Design queries that maximize information per tag.
- Solve for the GHASH key with fewer samples.
- Validate by forging a tag.

## Implementation Notes
Scripts: none (writeup-only challenge in this repo)
Data files: none

## Verification
No implementation is included; verify by comparing forgery success to the previous attack.
