# Challenge 34: MITM key-fixing attack on Diffie-Hellman with parameter injection
Set: 05 - Diffie-Hellman and friends
Cryptopals: https://cryptopals.com/sets/5/challenges/34
Run: `python scripts/run_challenge.py 34`

## Goal
Mount a MITM key-fixing attack on Diffie-Hellman with parameter injection.

## Cryptographic Insight
If an attacker replaces public values with p (or 0 mod p), the shared secret becomes 0. This lets the attacker derive the session key and decrypt traffic.

## Method
- Run a server and client that perform DH and exchange encrypted messages.
- Insert a MITM that replaces A and B with p.
- Derive the forced shared secret and decrypt the traffic.

## Detailed Walkthrough
The MITM key-fixing attack manipulates Diffie-Hellman parameters so the shared secret becomes predictable. By replacing public values with p, the shared secret becomes 0 for both sides.

With a known shared secret, the attacker can derive the same symmetric key and decrypt messages.

- Intercept and replace A and B with p.
- Both parties derive shared secret 0.
- Attacker decrypts messages using the predictable key.

## Implementation Notes
Scripts: server.py, attacker.py, client.py
Data files: none
Run order: start: server.py -> start: attacker.py -> run: client.py

## Verification
Run order: start server, start attacker, then run client to see decrypted messages.
