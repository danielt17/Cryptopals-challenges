# Challenge 32: Break HMAC-SHA1 with a slightly less artificial timing leak
Link: https://cryptopals.com/sets/4/challenges/32

## Goal
Recover an HMAC-SHA1 tag with a less artificial timing leak.

## Cryptographic Insight
Reducing the per-byte delay makes noise a factor. You need multiple samples or averaging to distinguish correct bytes from timing variance.

## Method
- Start the server with a smaller timing leak.
- For each candidate byte, take multiple timing samples.
- Select the byte with the best average and iterate.

## Implementation Notes
Scripts: server.py, attacker.py
Data files: none
Run order: start: server.py -> run: attacker.py

## Verification
Run order: start the server, then run the attacker to recover the MAC.
