# Challenge 46: RSA parity oracle
Set: 06 - RSA and DSA
Cryptopals: https://cryptopals.com/sets/6/challenges/46
Run: `python scripts/run_challenge.py 46`

## Goal
Use an RSA parity oracle to recover plaintext.

## Cryptographic Insight
If an oracle reveals the parity (odd/even) of the decrypted plaintext, you can binary search the plaintext by multiplying the ciphertext by 2^e mod N and narrowing bounds based on parity.

## Method
- Maintain an interval [low, high] for the plaintext value.
- Repeatedly query parity of 2^e * c mod N and halve the interval.
- Convert the final interval to the plaintext.

## Implementation Notes
Scripts: rsa_parity_oracle.py
Data files: none
Run: python scripts/run_challenge.py 46

## Verification
The script prints the recovered plaintext and checks it against the original.
