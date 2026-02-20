# Challenge 18: Implement CTR mode
Set: 03 - Block and stream crypto
Cryptopals: https://cryptopals.com/sets/3/challenges/18
Run: `python scripts/run_challenge.py 18`

## Goal
Implement AES-CTR mode.

## Cryptographic Insight
CTR turns a block cipher into a stream cipher by encrypting a nonce+counter to produce a keystream. The keystream is XORed with plaintext or ciphertext; encryption and decryption are identical operations.

## Method
- Construct a nonce and incrementing counter for each block.
- Encrypt nonce||counter with AES to produce keystream blocks.
- XOR keystream with input data to encrypt or decrypt.

## Detailed Walkthrough
CTR mode turns a block cipher into a stream cipher by encrypting successive counter values and XORing with the plaintext. The same operation is used for encryption and decryption.

The key concerns are correct counter construction and ensuring a unique nonce or counter sequence for each message.

- Build a keystream from nonce and counter.
- XOR the keystream with plaintext or ciphertext.
- Increment the counter per block.

## Implementation Notes
Scripts: aes_ctr_mode.py
Data files: none
Run: python scripts/run_challenge.py 18

## Verification
The script outputs the decrypted plaintext from the provided challenge input.
