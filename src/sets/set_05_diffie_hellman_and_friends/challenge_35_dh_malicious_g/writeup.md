# Challenge 35: DH with negotiated groups, malicious g
Set: 05 - Diffie-Hellman and friends
Cryptopals: https://cryptopals.com/sets/5/challenges/35
Run: `python scripts/run_challenge.py 35`

## Goal
Exploit malicious generator choices in Diffie-Hellman.

## Cryptographic Insight
If g is set to 1, p, or p-1, the shared secret collapses to a small set of values. The attacker can guess the secret by trying the few possibilities and checking the ciphertext.

## Method
- Negotiate DH with a malicious g value.
- Observe that the shared secret must be one of a small set.
- Try each candidate and decrypt the messages.

## Detailed Walkthrough
Malicious g attacks exploit the fact that Diffie-Hellman assumes g is a generator. If g is set to 1, p, or p-1, the shared secret falls into a small, predictable set.

The attacker can try the few possible keys and decrypt messages without solving discrete logs.

- Force g to 1, p, or p-1.
- Enumerate the tiny set of possible shared secrets.
- Derive keys and decrypt messages.

## Implementation Notes
Scripts: server.py, attacker.py, client.py
Data files: none
Run order: start: server.py -> start: attacker.py -> run: client.py

## Verification
Run order: start server, start attacker, then run client. The attacker prints recovered messages.
