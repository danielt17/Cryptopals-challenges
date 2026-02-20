# Challenge 28: Implement a SHA-1 keyed MAC
Set: 04 - Stream crypto and randomness
Cryptopals: https://cryptopals.com/sets/4/challenges/28
Run: `python scripts/run_challenge.py 28`

## Goal
Implement a SHA-1 keyed MAC.

## Cryptographic Insight
A keyed MAC can be built by hashing key || message with SHA-1. This is not HMAC, but it illustrates how Merkle-Damgard hashes can be used as MACs and why they are vulnerable to length extension.

## Method
- Concatenate the secret key with the message.
- Compute SHA-1 over the concatenated bytes.
- Return the hash as the MAC.

## Detailed Walkthrough
A keyed MAC built as SHA1(key || message) is a prefix MAC. It provides authenticity if the key is secret, but it is vulnerable to length extension because SHA1 is Merkle-Damgard.

The implementation focuses on a correct SHA1 and MAC construction so later challenges can exploit its structure.

- Implement SHA1 hashing.
- Compute MAC as SHA1(key || message).
- Verify by recomputing and comparing.

## Implementation Notes
Scripts: sha1_keyed_mac.py
Data files: none
Run: python scripts/run_challenge.py 28

## Verification
The script prints a MAC and validates it by recomputing the hash.
