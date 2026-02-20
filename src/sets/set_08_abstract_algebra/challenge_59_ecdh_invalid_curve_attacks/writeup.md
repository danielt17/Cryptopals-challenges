# Challenge 59: Elliptic Curve Diffie-Hellman and Invalid-Curve Attacks
Set: 08 - Abstract Algebra
Cryptopals: https://toadstyle.org/cryptopals/a0833e607878a80fdc0808f889c721b1.txt
Run: `python scripts/run_challenge.py 59`

## Goal
Implement ECDH and perform invalid-curve attacks.

## Cryptographic Insight
Elliptic curves form groups with point addition and scalar multiplication. If a peer accepts points that are not on the chosen curve, an attacker can use points from other curves with small subgroups to leak the secret scalar modulo small factors.

## Method
- Implement point addition, doubling, and scalar multiplication on a short Weierstrass curve.
- Perform an ECDH handshake and verify that n*G = O for the base point order.
- Find points on invalid curves with small subgroup orders and send them to the victim.
- Use MAC brute force to recover the secret modulo small factors and combine with CRT.

## Implementation Notes
Scripts: none (writeup-only challenge in this repo)
Data files: none

## Verification
Use the given curve parameters and provided invalid curves to test the attack.
