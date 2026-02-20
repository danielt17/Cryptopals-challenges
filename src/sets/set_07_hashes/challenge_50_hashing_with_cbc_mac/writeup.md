# Challenge 50: Hashing with CBC-MAC
Set: 07 - Hashes
Cryptopals: https://cryptopals.com/sets/7/challenges/50
Run: `python scripts/run_challenge.py 50`

## Goal
Demonstrate weaknesses in CBC-MAC for variable-length messages.

## Cryptographic Insight
CBC-MAC does not include the message length, so variable-length messages can be spliced to create a different message with the same MAC. Proper constructions include the length or use CMAC.

## Method
- Construct two messages that share a MAC by reusing intermediate chaining values.
- Show that a longer message can be forged from a shorter one.
- Explain how including length would prevent the attack.

## Detailed Walkthrough
When CBC-MAC is used as a hash, it inherits malleability issues. By choosing message prefixes and adjusting subsequent blocks, an attacker can create collisions or make a forged file hash to a chosen value.

The challenge demonstrates a practical collision construction using the CBC-MAC chaining property.

- Exploit the XOR chaining between blocks.
- Adjust blocks so the internal state collides.
- Produce two different files with the same MAC.

## Implementation Notes
Scripts: hashing_with_cbc_mac.py
Data files: none
Run: python scripts/run_challenge.py 50

## Verification
The script prints a forged message whose MAC verifies under the same key.
