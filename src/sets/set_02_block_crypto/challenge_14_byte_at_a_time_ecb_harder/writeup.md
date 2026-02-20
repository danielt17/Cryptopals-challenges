# Challenge 14: Byte-at-a-time ECB decryption (harder)
Link: https://cryptopals.com/sets/2/challenges/14

## Goal
Recover an unknown suffix with a random-length prefix in front of your input.

## Cryptographic Insight
A random prefix breaks simple block alignment. By finding where your controlled bytes align to block boundaries, you can recover the prefix length and resume the byte-at-a-time ECB attack.

## Method
- Send crafted inputs to detect when two identical adjacent blocks appear, indicating alignment.
- Compute the prefix length offset to align your controlled bytes.
- Use the byte-at-a-time dictionary attack on the aligned blocks.

## Implementation Notes
Scripts: byte_at_a_time_ecb_harder.py
Data files: none
Run: python scripts/run_challenge.py 14

## Verification
The script prints the recovered plaintext once alignment is found.
