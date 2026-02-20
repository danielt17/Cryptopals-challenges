# Challenge 17: The CBC padding oracle
Set: 03 - Block and stream crypto
Cryptopals: https://cryptopals.com/sets/3/challenges/17
Run: `python scripts/run_challenge.py 17`

## Goal
Use a CBC padding oracle to decrypt a ciphertext without the key.

## Cryptographic Insight
If a system reveals whether padding is valid, you can recover plaintext by manipulating the previous ciphertext block to force chosen padding values. This leaks each byte with a small number of queries.

## Method
- Split ciphertext into blocks and target one block at a time.
- For each byte position, craft a modified previous block that yields a valid padding value.
- Infer the plaintext byte from the padding condition and repeat.

## Detailed Walkthrough
The CBC padding oracle reveals whether decrypted plaintext has valid PKCS#7 padding. That single bit of information is enough to decrypt the message byte by byte.

The attack works from the end of each block, modifying the previous ciphertext block to force a chosen padding value and observing when the oracle accepts the padding.

- Work from the last byte of each block to the first.
- Modify the previous block to force a padding guess.
- Repeat for all blocks to recover the full plaintext.

## Implementation Notes
Scripts: cbc_padding_oracle.py
Data files: none
Run: python scripts/run_challenge.py 17

## Verification
The script prints the recovered plaintext after iterating over all blocks.
