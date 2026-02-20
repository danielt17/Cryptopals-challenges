# Challenge 29: Break a SHA-1 keyed MAC using length extension
Link: https://cryptopals.com/sets/4/challenges/29

## Goal
Forge a SHA-1 MAC using length extension.

## Cryptographic Insight
Merkle-Damgard hashes are vulnerable to length extension: given H(key || message), an attacker can append data and compute H(key || message || padding || extension) without knowing the key.

## Method
- Guess the key length and compute the glue padding for key||message.
- Initialize SHA-1 state from the known digest and resume hashing the extension.
- Construct the forged message and MAC and validate with the oracle.

## Implementation Notes
Scripts: sha1_length_extension.py
Data files: none
Run: python scripts/run_challenge.py 29

## Verification
The script prints a forged MAC that verifies under the unknown key.
