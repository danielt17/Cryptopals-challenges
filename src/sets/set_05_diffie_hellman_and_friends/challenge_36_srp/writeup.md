# Challenge 36: Implement Secure Remote Password (SRP)
Set: 05 - Diffie-Hellman and friends
Cryptopals: https://cryptopals.com/sets/5/challenges/36
Run: `python scripts/run_challenge.py 36`

## Goal
Implement the Secure Remote Password (SRP) protocol.

## Cryptographic Insight
SRP is a password-authenticated key exchange that avoids sending the password or password-equivalent data. Both sides compute a shared secret using salts, a verifier, and the scrambling parameter u.

## Method
- Server stores a salt and verifier v = g^x for x derived from the password.
- Client and server exchange A and B and compute u.
- Both derive the same session key and verify with an HMAC.

## Detailed Walkthrough
Secure Remote Password (SRP) authenticates a password without revealing it. The server stores a verifier v = g^x mod N and a salt. The client and server exchange A and B, compute a scrambling parameter u, and derive a shared session key.

Both sides prove knowledge of the key via HMAC. Correct handling of parameters, salt, and modular arithmetic is essential.

- Compute x from salt and password, store verifier v.
- Exchange A, B, and u to derive the shared secret.
- Verify HMACs to authenticate the session.

## Implementation Notes
Scripts: server.py, client.py, utils.py
Data files: none
Run order: start: server.py -> run: client.py

## Verification
Run order: start server, then run client to see successful authentication.
