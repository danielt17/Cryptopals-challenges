# Challenge 65: Truncated-MAC GCM Revisited: Improving the Key-Recovery Attack
Link: https://toadstyle.org/cryptopals/a1a2e7311ec5f2535ec46eaebd4588f0.txt

## Goal
Improve the truncated GCM attack using ciphertext length extension.

## Cryptographic Insight
If the last ciphertext block is partial, you can tweak the length block to gain additional degrees of freedom. This turns the homogeneous system T*d = 0 into T*d = t, letting you force more rows to zero and accelerate key recovery.

## Method
- Detect when the last ciphertext block is incomplete.
- Adjust the length block to introduce a controlled offset.
- Solve the linear system for a particular solution and add null-space vectors.
- Use the improved degrees of freedom to forge more efficiently.

## Implementation Notes
Scripts: none (writeup-only challenge in this repo)
Data files: none

## Verification
No implementation is included; verify by comparing forgery success to the previous attack.
