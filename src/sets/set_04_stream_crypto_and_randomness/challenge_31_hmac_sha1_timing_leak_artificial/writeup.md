# Challenge 31: Implement and break HMAC-SHA1 with an artificial timing leak
Set: 04 - Stream crypto and randomness
Cryptopals: https://cryptopals.com/sets/4/challenges/31
Run: `python scripts/run_challenge.py 31`

## Goal
Recover an HMAC-SHA1 tag using an artificial timing leak.

## Cryptographic Insight
A byte-by-byte comparison with a fixed delay per matched byte leaks timing information. By measuring response time, an attacker can infer correct bytes of the MAC incrementally.

## Method
- Start the vulnerable server that compares HMACs byte-by-byte with a delay.
- For each byte position, try all 256 values and measure response time.
- Choose the byte that yields the longest response and proceed.

## Detailed Walkthrough
A timing leak in a naive MAC comparison can reveal the correct signature byte by byte. If the server sleeps after each matching byte, the total response time leaks how many bytes matched.

The attacker measures response times for each candidate byte, chooses the slowest, and repeats for the next byte.

- Send signatures with a fixed prefix guess.
- Pick the byte that yields the longest response time.
- Repeat to recover the full MAC.

## Implementation Notes
Scripts: utils.py, server.py, attacker.py
Data files: none
Run order: start: server.py -> run: attacker.py

## Verification
Run order: start the server, then run the attacker to recover the MAC.
