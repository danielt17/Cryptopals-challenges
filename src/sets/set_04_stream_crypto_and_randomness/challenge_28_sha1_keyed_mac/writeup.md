# Challenge 28: Implement a SHA-1 keyed MAC
Link: https://cryptopals.com/sets/4/challenges/28

## Goal
Implement a SHA-1 keyed MAC.

## Cryptographic Insight
A keyed MAC can be built by hashing key || message with SHA-1. This is not HMAC, but it illustrates how Merkle-Damgard hashes can be used as MACs and why they are vulnerable to length extension.

## Method
- Concatenate the secret key with the message.
- Compute SHA-1 over the concatenated bytes.
- Return the hash as the MAC.

## Implementation Notes
Scripts: sha1_keyed_mac.py
Data files: none
Run: python scripts/run_challenge.py 28

## Verification
The script prints a MAC and validates it by recomputing the hash.
