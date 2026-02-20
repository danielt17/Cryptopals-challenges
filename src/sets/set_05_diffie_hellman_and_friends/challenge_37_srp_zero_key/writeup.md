# Challenge 37: Break SRP with a zero key
Set: 05 - Diffie-Hellman and friends
Cryptopals: https://cryptopals.com/sets/5/challenges/37
Run: `python scripts/run_challenge.py 37`

## Goal
Break SRP by forcing a zero shared key.

## Cryptographic Insight
If the client sends A = 0 (or a multiple of N), the shared secret becomes 0 regardless of the password, letting an attacker forge the HMAC and authenticate.

## Method
- Send a crafted public value A that is 0 mod N.
- Compute the resulting shared secret (zero) and session key.
- Forge the HMAC and bypass authentication.

## Detailed Walkthrough
SRP can be broken if the server accepts A values that force the session key to zero. If a client sends A = 0, A = N, or A = kN, the server computes S = 0 and the session key becomes predictable.

The attacker can then forge the HMAC without knowing the password.

- Send a public value that is 0 mod N.
- Both sides compute session key 0.
- Forge the HMAC and authenticate.

## Implementation Notes
Scripts: server.py, client_setup_then_attack.py
Data files: none
Run order: start: server.py -> run: client_setup_then_attack.py

## Verification
Run order: start server, then run the client/attacker to see the bypass.
