# Challenge 62: Key-Recovery Attacks on ECDSA with Biased Nonces
Set: 08 - Abstract Algebra
Cryptopals: https://toadstyle.org/cryptopals/76f2e314809b2a34ce9ff0d2a08f7a7f.txt
Run: `python scripts/run_challenge.py 62`

## Goal
Recover an ECDSA private key from biased nonces using lattice reduction.

## Cryptographic Insight
If the nonce k has known low bits (bias), the signature equations yield approximate linear relations in the secret key. These relations define a lattice where the secret appears as a short vector. LLL reduction can recover that vector.

## Method
- Generate signatures with a nonce whose low bits are zero.
- Transform each signature into (t, u) values yielding d*t ~= u.
- Build a lattice basis encoding these approximations and run LLL.
- Extract the secret key from a short vector in the reduced basis.

## Detailed Walkthrough
ECDSA nonces must be uniformly random. If nonces are biased (for example, some bits are fixed or leak), lattice attacks can recover the private key from a set of signatures.

The challenge studies how partial information about k translates into a full key recovery.

- Collect signatures with biased nonces.
- Form a lattice instance from the ECDSA equations.
- Solve for the private key using lattice reduction.

## Implementation Notes
Scripts: none (writeup-only challenge in this repo)
Data files: none

## Verification
Verify by recomputing the public key from the recovered secret.
