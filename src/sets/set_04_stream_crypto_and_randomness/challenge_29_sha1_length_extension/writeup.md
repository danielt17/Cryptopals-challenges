# Challenge 29: Break a SHA-1 keyed MAC using length extension
Set: 04 - Stream crypto and randomness
Cryptopals: https://cryptopals.com/sets/4/challenges/29
Run: `python scripts/run_challenge.py 29`

## Goal
Forge a SHA-1 MAC using length extension.

## Cryptographic Insight
Merkle-Damgard hashes are vulnerable to length extension: given H(key || message), an attacker can append data and compute H(key || message || padding || extension) without knowing the key.

## Method
- Guess the key length and compute the glue padding for key||message.
- Initialize SHA-1 state from the known digest and resume hashing the extension.
- Construct the forged message and MAC and validate with the oracle.

## Detailed Walkthrough
Length extension attacks exploit Merkle-Damgard hashes. Given SHA1(key || message) and the message length, you can compute SHA1(key || message || padding || suffix) without the key.

The attack guesses the key length, reconstructs the padding, and continues hashing from the internal state.

- Guess key length to reconstruct padding.
- Initialize SHA1 with the known digest as state.
- Hash the attacker-controlled suffix to forge a new MAC.

## Implementation Notes
Scripts: sha1_length_extension.py
Data files: none
Run: python scripts/run_challenge.py 29

## Verification
The script prints a forged MAC that verifies under the unknown key.
