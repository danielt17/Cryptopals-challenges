# Challenge 13: ECB cut-and-paste
Link: https://cryptopals.com/sets/2/challenges/13

## Goal
Exploit ECB block independence to forge an admin profile.

## Cryptographic Insight
ECB encrypts blocks independently, so swapping blocks in ciphertext produces predictable block-level changes in plaintext. By crafting inputs with aligned blocks, you can splice an 'admin' block into a valid profile.

## Method
- Craft an email input that causes 'admin' plus padding to align to a block boundary.
- Encrypt it to obtain the 'admin' block.
- Craft a normal profile ciphertext and replace the role block with the admin block.

## Implementation Notes
Scripts: ecb_cut_and_paste.py
Data files: none
Run: python scripts/run_challenge.py 13

## Verification
The script outputs a forged profile that parses as admin.
