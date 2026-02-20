# Challenge 63: Key-Recovery Attacks on GCM with Repeated Nonces
Set: 08 - Abstract Algebra
Cryptopals: https://toadstyle.org/cryptopals/2dfbf7e58fd43c140b62485f8d90bebe.txt
Run: `python scripts/run_challenge.py 63`

## Goal
Recover the GCM authentication key from repeated nonces.

## Cryptographic Insight
GCM's MAC is a polynomial in the authentication key h over GF(2^128). Reusing a nonce reuses the mask, so subtracting two tags eliminates the mask and yields a polynomial with h as a root. Factoring this polynomial reveals h.

## Method
- Implement GF(2^128) arithmetic and the GHASH function.
- Collect two messages encrypted under the same nonce.
- Build the difference polynomial and factor it to find candidate h values.
- Test candidates by forging a valid tag.

## Detailed Walkthrough
GCM breaks catastrophically if a nonce is reused with the same key. Reuse reveals the XOR of plaintexts and produces equations over GHASH that can reveal the authentication subkey.

Once the GHASH key is recovered, tags can be forged for arbitrary messages.

- Detect nonce reuse across messages.
- Use GHASH linearity to solve for the authentication key.
- Forge tags and decrypt or modify messages.

## Implementation Notes
Scripts: none (writeup-only challenge in this repo)
Data files: none

## Verification
No implementation is included; verify by recovering h and forging a tag.
