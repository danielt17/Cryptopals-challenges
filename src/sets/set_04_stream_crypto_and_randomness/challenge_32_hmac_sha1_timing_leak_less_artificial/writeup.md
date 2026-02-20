# Challenge 32: Break HMAC-SHA1 with a slightly less artificial timing leak
Set: 04 - Stream crypto and randomness
Cryptopals: https://cryptopals.com/sets/4/challenges/32
Run: `python scripts/run_challenge.py 32`

## Goal
Recover an HMAC-SHA1 tag with a less artificial timing leak.

## Cryptographic Insight
Reducing the per-byte delay makes noise a factor. You need multiple samples or averaging to distinguish correct bytes from timing variance.

## Method
- Start the server with a smaller timing leak.
- For each candidate byte, take multiple timing samples.
- Select the byte with the best average and iterate.

## Detailed Walkthrough
## Set 5: Diffie-Hellman and friends

This challenge makes the timing leak less obvious by reducing or randomizing the delay. The same basic attack still works, but it requires multiple samples and statistical averaging.

Robust attacks measure each candidate many times and select the byte with the best average timing.

- Run repeated measurements per candidate byte.
- Use averages or medians to reduce noise.
- Recover the MAC byte by byte.

## Implementation Notes
Scripts: server.py, attacker.py
Data files: none
Run order: start: server.py -> run: attacker.py

## Verification
Run order: start the server, then run the attacker to recover the MAC.
