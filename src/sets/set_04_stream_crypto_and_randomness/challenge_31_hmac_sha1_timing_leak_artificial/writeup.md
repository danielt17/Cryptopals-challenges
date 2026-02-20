# Challenge 31: Implement and break HMAC-SHA1 with an artificial timing leak
Link: https://cryptopals.com/sets/4/challenges/31

## Goal
Recover an HMAC-SHA1 tag using an artificial timing leak.

## Cryptographic Insight
A byte-by-byte comparison with a fixed delay per matched byte leaks timing information. By measuring response time, an attacker can infer correct bytes of the MAC incrementally.

## Method
- Start the vulnerable server that compares HMACs byte-by-byte with a delay.
- For each byte position, try all 256 values and measure response time.
- Choose the byte that yields the longest response and proceed.

## Implementation Notes
Scripts: utils.py, server.py, attacker.py
Data files: none
Run order: start: server.py -> run: attacker.py

## Verification
Run order: start the server, then run the attacker to recover the MAC.
