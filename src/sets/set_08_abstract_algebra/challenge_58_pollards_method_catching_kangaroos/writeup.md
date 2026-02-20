# Challenge 58: Pollard's Method for Catching Kangaroos
Link: https://toadstyle.org/cryptopals/3e17c7b35fcf491d08c989081ed18c9a.txt

## Goal
Use Pollard's kangaroo to recover discrete logs in a known interval.

## Cryptographic Insight
Pollard's kangaroo (lambda) algorithm finds the discrete log of y in a range [a, b] using two pseudorandom walks (tame and wild). It is efficient in time and constant in memory, and can be applied to recover the remaining bits of a DH secret after partial leakage.

## Method
- Define a deterministic step function f(y) that chooses the next jump size.
- Run the tame kangaroo from g^b and record its final position.
- Run the wild kangaroo from y and stop when it collides with the tame path.
- Apply the algorithm to recover remaining bits of a key after subgroup leakage.

## Implementation Notes
Scripts: none (writeup-only challenge in this repo)
Data files: none

## Verification
No implementation is included; verify by solving the provided sample discrete log intervals.
