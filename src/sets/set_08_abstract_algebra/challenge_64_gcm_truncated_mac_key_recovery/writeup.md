# Challenge 64: Key-Recovery Attacks on GCM with a Truncated MAC
Link: https://toadstyle.org/cryptopals/1d79ee513b73e1e0367eae2297e9f234.txt

## Goal
Exploit truncated GCM tags to forge and recover the authentication key.

## Cryptographic Insight
Multiplication and squaring in GF(2^128) are linear in the bits of h. By flipping carefully chosen ciphertext blocks, you can force rows of the resulting linear system to zero, improving forgery probability. Each successful forgery yields linear constraints on h, shrinking the key space.

## Method
- Model multiplication and squaring as linear transformations on bit vectors.
- Build a matrix capturing how bit flips affect the MAC difference.
- Find null-space vectors to force MAC rows to zero and forge tags.
- Accumulate linear constraints on h to narrow the key space.

## Implementation Notes
Scripts: none (writeup-only challenge in this repo)
Data files: none

## Verification
No implementation is included; verify by increasing forgery success and recovering h.
