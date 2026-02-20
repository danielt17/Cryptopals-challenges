# Challenge 38: Offline dictionary attack on simplified SRP
Set: 05 - Diffie-Hellman and friends
Cryptopals: https://cryptopals.com/sets/5/challenges/38
Run: `python scripts/run_challenge.py 38`

## Goal
Perform an offline dictionary attack on simplified SRP.

## Cryptographic Insight
A malicious server can force parameters that let it verify password guesses offline. The client will compute an HMAC over a key derived from the password, which the attacker can test against a dictionary.

## Method
- Run a fake server that sends crafted parameters and captures the client's HMAC.
- Iterate over a password dictionary, recomputing the expected HMAC.
- Select the password that matches the client's HMAC.

## Implementation Notes
Scripts: fake_server.py, client.py, server.py
Data files: none
Run order: start: fake_server.py -> run: client.py

## Verification
Run order: start fake_server, then run client. The attacker prints the recovered password.
