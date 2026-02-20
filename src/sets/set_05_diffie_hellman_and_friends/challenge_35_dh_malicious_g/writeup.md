# Challenge 35: DH with negotiated groups, malicious g
Link: https://cryptopals.com/sets/5/challenges/35

## Goal
Exploit malicious generator choices in Diffie-Hellman.

## Cryptographic Insight
If g is set to 1, p, or p-1, the shared secret collapses to a small set of values. The attacker can guess the secret by trying the few possibilities and checking the ciphertext.

## Method
- Negotiate DH with a malicious g value.
- Observe that the shared secret must be one of a small set.
- Try each candidate and decrypt the messages.

## Implementation Notes
Scripts: server.py, attacker.py, client.py
Data files: none
Run order: start: server.py -> start: attacker.py -> run: client.py

## Verification
Run order: start server, start attacker, then run client. The attacker prints recovered messages.
