# Challenge 49: CBC-MAC message forgery
Set: 07 - Hashes
Cryptopals: https://cryptopals.com/sets/7/challenges/49
Run: `python scripts/run_challenge.py 49`

## Goal
Forge CBC-MACs under different IV assumptions.

## Cryptographic Insight
CBC-MAC is secure for fixed-length messages with a fixed IV. If the attacker can choose the IV or the message length is variable, CBC-MAC becomes malleable and forgery is possible by splicing or adjusting blocks.

## Method
- For the IV-controlled variant, choose an IV to neutralize differences in the first block.
- For the fixed-IV variant, use message concatenation and length manipulation to forge a valid MAC.
- Verify that the forged message validates under the MAC.

## Implementation Notes
Scripts: iv_control.py, no_iv_control.py
Data files: none
Run order: run: iv_control.py -> run: no_iv_control.py

## Verification
The two scripts demonstrate the IV-controlled and no-IV-control cases.
