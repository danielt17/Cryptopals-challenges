# Challenge 34: MITM key-fixing attack on Diffie-Hellman with parameter injection
Link: https://cryptopals.com/sets/5/challenges/34

## Goal
Mount a MITM key-fixing attack on Diffie-Hellman with parameter injection.

## Cryptographic Insight
If an attacker replaces public values with p (or 0 mod p), the shared secret becomes 0. This lets the attacker derive the session key and decrypt traffic.

## Method
- Run a server and client that perform DH and exchange encrypted messages.
- Insert a MITM that replaces A and B with p.
- Derive the forced shared secret and decrypt the traffic.

## Implementation Notes
Scripts: server.py, attacker.py, client.py
Data files: none
Run order: start: server.py -> start: attacker.py -> run: client.py

## Verification
Run order: start server, start attacker, then run client to see decrypted messages.
