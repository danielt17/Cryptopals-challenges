# Challenge 66: Exploiting Implementation Errors in Diffie-Hellman
Set: 08 - Abstract Algebra
Cryptopals: https://toadstyle.org/cryptopals/66.txt
Run: `python scripts/run_challenge.py 66`

## Goal
Recover Diffie-Hellman secrets via deterministic fault injection.

## Cryptographic Insight
A deterministic fault in scalar multiplication leaks information about the secret exponent. By crafting points that fault on specific add() steps, an attacker can learn key bits from an oracle that reports faults.

## Method
- Implement scalar multiplication with a deterministic fault predicate.
- Search for points that trigger a fault on one branch of the bit decision tree.
- Query the oracle to distinguish bits based on whether a fault occurs.
- Iterate to recover the secret, using kangaroo if needed for the remainder.

## Detailed Walkthrough
# License

Everything in this repository is distributed under the terms of the MIT License. See file "LICENSE" for further reference.

Diffie-Hellman implementation errors typically involve failing to validate public keys or group membership. Accepting invalid public keys can force computation in small subgroups or even reveal private exponents.

The fix is straightforward: validate inputs, enforce subgroup membership, and reject out-of-range values.

- Check that public values are in the correct range.
- Verify subgroup membership or use safe primes.
- Reject invalid parameters before computing secrets.

## Implementation Notes
Scripts: none (writeup-only challenge in this repo)
Data files: none

## Verification
No implementation is included; validate by recovering a secret scalar in a simulated oracle.
