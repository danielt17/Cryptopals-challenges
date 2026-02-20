# Challenge 37: Break SRP with a zero key
Link: https://cryptopals.com/sets/5/challenges/37

## Goal
Break SRP by forcing a zero shared key.

## Cryptographic Insight
If the client sends A = 0 (or a multiple of N), the shared secret becomes 0 regardless of the password, letting an attacker forge the HMAC and authenticate.

## Method
- Send a crafted public value A that is 0 mod N.
- Compute the resulting shared secret (zero) and session key.
- Forge the HMAC and bypass authentication.

## Implementation Notes
Scripts: server.py, client_setup_then_attack.py
Data files: none
Run order: start: server.py -> run: client_setup_then_attack.py

## Verification
Run order: start server, then run the client/attacker to see the bypass.
