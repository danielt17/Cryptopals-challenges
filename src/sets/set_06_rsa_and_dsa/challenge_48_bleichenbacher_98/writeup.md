# Challenge 48: Bleichenbacher 98 attack (TLS)
Set: 06 - RSA and DSA
Cryptopals: https://cryptopals.com/sets/6/challenges/48
Run: `python scripts/run_challenge.py 48`

## Goal
Perform Bleichenbacher's 98 attack against a TLS-like padding oracle.

## Cryptographic Insight
This attack adapts the PKCS#1 v1.5 padding oracle to the TLS handshake. A MITM observes and manipulates encrypted premaster secrets, using oracle responses to recover the secret and decrypt traffic.

## Method
- Run a TLS-like server and client that exchange encrypted premaster secrets.
- Interpose a MITM that queries a padding oracle to recover the premaster secret.
- Use the recovered secret to derive session keys and decrypt messages.

## Detailed Walkthrough
## Set 7: Hashes

This is a full Bleichenbacher 98 attack against an RSA-based TLS handshake. The attacker uses the padding oracle to recover the premaster secret, then derives the session keys.

The implementation simulates the TLS key exchange and applies the same interval-narrowing attack as in the previous challenge, but in a more realistic protocol context.

- Capture an RSA-encrypted premaster secret.
- Query the padding oracle to narrow candidates.
- Recover the premaster secret and derive session keys.

## Implementation Notes
Scripts: server.py, attacker.py, client.py
Data files: none
Run order: start: server.py -> start: attacker.py -> run: client.py

## Verification
Run order: start server, start attacker, then run client. The attacker logs recovered secrets.
