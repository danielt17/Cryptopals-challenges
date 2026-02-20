# Challenge 36: Implement Secure Remote Password (SRP)
Link: https://cryptopals.com/sets/5/challenges/36

## Goal
Implement the Secure Remote Password (SRP) protocol.

## Cryptographic Insight
SRP is a password-authenticated key exchange that avoids sending the password or password-equivalent data. Both sides compute a shared secret using salts, a verifier, and the scrambling parameter u.

## Method
- Server stores a salt and verifier v = g^x for x derived from the password.
- Client and server exchange A and B and compute u.
- Both derive the same session key and verify with an HMAC.

## Implementation Notes
Scripts: server.py, client.py, utils.py
Data files: none
Run order: start: server.py -> run: client.py

## Verification
Run order: start server, then run client to see successful authentication.
