# Challenge 47: Bleichenbacher's PKCS 1.5 padding oracle
Set: 06 - RSA and DSA
Cryptopals: https://cryptopals.com/sets/6/challenges/47
Run: `python scripts/run_challenge.py 47`

## Goal
Exploit a PKCS#1 v1.5 padding oracle to decrypt RSA ciphertexts.

## Cryptographic Insight
Bleichenbacher's attack uses a padding oracle to iteratively narrow the range of possible plaintexts. Each query finds a multiplier that yields a conforming padding and tightens the interval of candidates.

## Method
- Query the oracle to find an initial s such that c * s^e has valid padding.
- Maintain intervals of possible plaintext values and update them with each valid s.
- Iterate until the interval collapses to a single plaintext.

## Detailed Walkthrough
PKCS#1 v1.5 padding oracle attacks use an oracle that only tells you whether the decrypted plaintext has the correct 0x0002 padding format. Bleichenbacher's 98 algorithm narrows a set of possible plaintext intervals until only one remains.

This challenge implements the oracle and the interval-narrowing search for RSA-256 and RSA-2048.

- Use the padding oracle to test candidate multipliers.
- Maintain and narrow the interval of possible plaintexts.
- Recover the exact plaintext once the interval collapses.

## Implementation Notes
Scripts: pkcs1_v1_5_padding_oracle_rsa256.py, pkcs1_v1_5_padding_oracle_rsa2048.py
Data files: none
Run order: run: pkcs1_v1_5_padding_oracle_rsa256.py -> run: pkcs1_v1_5_padding_oracle_rsa2048.py

## Verification
The scripts demonstrate the attack for RSA-256 and RSA-2048 variants.
