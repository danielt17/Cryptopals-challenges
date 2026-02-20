# Challenge 45: DSA parameter tampering
Set: 06 - RSA and DSA
Cryptopals: https://cryptopals.com/sets/6/challenges/45
Run: `python scripts/run_challenge.py 45`

## Goal
Exploit DSA parameter tampering to forge signatures.

## Cryptographic Insight
If the generator g is set to 0 or 1, the signature verification equation becomes trivial. An attacker can create signatures that verify for any message without the private key.

## Method
- Select an unsafe g value (0 or 1 mod p).
- Generate a signature pair (r, s) that satisfies the verifier's equation.
- Verify that the signature passes without the private key.

## Detailed Walkthrough
DSA parameter tampering shows that choosing a malicious generator g can break security. If g = 0, signatures are trivially valid. If g = p + 1, signatures can be forged for any message.

The lesson is to validate DSA parameters or use standardized ones.

- Choose a malicious g value.
- Forge signatures that pass verification.
- Demonstrate why parameter validation matters.

## Implementation Notes
Scripts: dsa_parameter_tampering.py
Data files: none
Run: python scripts/run_challenge.py 45

## Verification
The script demonstrates a forged signature under tampered parameters.
