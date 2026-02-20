# Challenge 41: Unpadded message recovery oracle
Set: 06 - RSA and DSA
Cryptopals: https://cryptopals.com/sets/6/challenges/41
Run: `python scripts/run_challenge.py 41`

## Goal
Exploit RSA's multiplicative property to recover plaintext using an oracle.

## Cryptographic Insight
RSA is multiplicative: (m * s)^e = m^e * s^e mod N. If you can get a decryption of a modified ciphertext, you can divide out the modifier and recover the original plaintext.

## Method
- Choose a random multiplier s and compute c' = c * s^e mod N.
- Query the oracle to decrypt c'.
- Divide by s mod N to recover the original plaintext.

## Detailed Walkthrough
Unpadded RSA is multiplicatively homomorphic: (m * s)^e mod n = c * s^e mod n. If an oracle decrypts ciphertexts, you can recover m by sending a modified ciphertext and dividing out s.

The attack does not require factoring n, only an oracle that will decrypt arbitrary ciphertexts.

- Choose a multiplier s and compute c' = c * s^e mod n.
- Ask the oracle to decrypt c'.
- Divide by s to recover the original message.

## Implementation Notes
Scripts: unpadded_rsa_message_recovery.py
Data files: none
Run: python scripts/run_challenge.py 41

## Verification
The script prints the recovered message and confirms it matches the original.
