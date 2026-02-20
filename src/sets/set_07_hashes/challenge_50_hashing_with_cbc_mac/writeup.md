# Challenge 50: Hashing with CBC-MAC
Link: https://cryptopals.com/sets/7/challenges/50

## Goal
Demonstrate weaknesses in CBC-MAC for variable-length messages.

## Cryptographic Insight
CBC-MAC does not include the message length, so variable-length messages can be spliced to create a different message with the same MAC. Proper constructions include the length or use CMAC.

## Method
- Construct two messages that share a MAC by reusing intermediate chaining values.
- Show that a longer message can be forged from a shorter one.
- Explain how including length would prevent the attack.

## Implementation Notes
Scripts: hashing_with_cbc_mac.py
Data files: none
Run: python scripts/run_challenge.py 50

## Verification
The script prints a forged message whose MAC verifies under the same key.
