# Challenge 30: Break an MD4 keyed MAC using length extension
Link: https://cryptopals.com/sets/4/challenges/30

## Goal
Forge MD4-based (and MD5-based) MACs via length extension.

## Cryptographic Insight
MD4 (and MD5) are Merkle-Damgard hashes and have the same length extension property. By injecting internal state and padding, you can append data and compute a valid MAC without the key.

## Method
- Reconstruct the MD4/MD5 internal state from the known digest.
- Append correct padding for the unknown key length.
- Continue hashing the extension to produce a forged MAC.

## Implementation Notes
Scripts: md4_length_extension.py, md5_length_extension.py
Data files: none
Run order: run: md4_length_extension.py -> run: md5_length_extension.py

## Verification
The scripts print forged MACs for both MD4 and MD5 variants.
