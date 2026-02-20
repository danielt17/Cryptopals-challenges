# Challenge 13: ECB cut-and-paste
Set: 02 - Block crypto
Cryptopals: https://cryptopals.com/sets/2/challenges/13
Run: `python scripts/run_challenge.py 13`

## Goal
Exploit ECB block independence to forge an admin profile.

## Cryptographic Insight
ECB encrypts blocks independently, so swapping blocks in ciphertext produces predictable block-level changes in plaintext. By crafting inputs with aligned blocks, you can splice an 'admin' block into a valid profile.

## Method
- Craft an email input that causes 'admin' plus padding to align to a block boundary.
- Encrypt it to obtain the 'admin' block.
- Craft a normal profile ciphertext and replace the role block with the admin block.

## Detailed Walkthrough
ECB cut-and-paste demonstrates that ECB mode is malleable at the block level. A user profile is encoded as key-value pairs and encrypted under ECB, which means blocks can be copied and rearranged without detection.

The attack crafts one ciphertext block that decrypts to "admin" with valid padding and then splices it into a normal profile ciphertext where the role field begins on a block boundary.

- Sanitize user input to remove separators.
- Align "admin" to a fresh block with padding.
- Replace the role block with the "admin" block.

## Implementation Notes
Scripts: ecb_cut_and_paste.py
Data files: none
Run: python scripts/run_challenge.py 13

## Verification
The script outputs a forged profile that parses as admin.
