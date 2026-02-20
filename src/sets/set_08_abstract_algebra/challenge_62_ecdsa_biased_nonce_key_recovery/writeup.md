# Challenge 62: Key-Recovery Attacks on ECDSA with Biased Nonces
Link: https://toadstyle.org/cryptopals/76f2e314809b2a34ce9ff0d2a08f7a7f.txt

## Goal
Recover an ECDSA private key from biased nonces using lattice reduction.

## Cryptographic Insight
If the nonce k has known low bits (bias), the signature equations yield approximate linear relations in the secret key. These relations define a lattice where the secret appears as a short vector. LLL reduction can recover that vector.

## Method
- Generate signatures with a nonce whose low bits are zero.
- Transform each signature into (t, u) values yielding d*t ~= u.
- Build a lattice basis encoding these approximations and run LLL.
- Extract the secret key from a short vector in the reduced basis.

## Implementation Notes
Scripts: none (writeup-only challenge in this repo)
Data files: none

## Verification
Verify by recomputing the public key from the recovered secret.
