# Challenge 66: Exploiting Implementation Errors in Diffie-Hellman
Link: https://toadstyle.org/cryptopals/66.txt

## Goal
Recover Diffie-Hellman secrets via deterministic fault injection.

## Cryptographic Insight
A deterministic fault in scalar multiplication leaks information about the secret exponent. By crafting points that fault on specific add() steps, an attacker can learn key bits from an oracle that reports faults.

## Method
- Implement scalar multiplication with a deterministic fault predicate.
- Search for points that trigger a fault on one branch of the bit decision tree.
- Query the oracle to distinguish bits based on whether a fault occurs.
- Iterate to recover the secret, using kangaroo if needed for the remainder.

## Implementation Notes
Scripts: none (writeup-only challenge in this repo)
Data files: none

## Verification
No implementation is included; validate by recovering a secret scalar in a simulated oracle.
