# Challenge 57: Diffie-Hellman Revisited: Subgroup-Confinement Attacks
Set: 08 - Abstract Algebra
Cryptopals: https://toadstyle.org/cryptopals/513b590b41d19eff3a0aa028023349fd.txt
Run: `python scripts/run_challenge.py 57`

## Goal
Recover a Diffie-Hellman private key using subgroup confinement attacks.

## Cryptographic Insight
If the group has small subgroups, an attacker can send a small-order element h. The victim computes a shared secret h^x that can take only r values, where r is the subgroup order. A MAC on that secret lets the attacker brute force x mod r. Repeating for multiple r values yields x via CRT.

## Method
- Factor j = (p-1)/q to find small subgroup orders r.
- Construct a small-order element h = rand^((p-1)/r) mod p.
- Send h as the public key and brute force the MAC to recover x mod r.
- Repeat for multiple r and combine residues with CRT to recover x.

## Implementation Notes
Scripts: none (writeup-only challenge in this repo)
Data files: none

## Verification
This repo does not include code for the attack; use the writeup to guide an implementation.
