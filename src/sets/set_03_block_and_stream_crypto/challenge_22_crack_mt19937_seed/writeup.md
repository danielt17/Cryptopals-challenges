# Challenge 22: Crack an MT19937 seed
Set: 03 - Block and stream crypto
Cryptopals: https://cryptopals.com/sets/3/challenges/22
Run: `python scripts/run_challenge.py 22`

## Goal
Recover the MT19937 seed from a time-based initialization.

## Cryptographic Insight
If MT19937 is seeded with the current time, the seed space is small. You can brute force candidate timestamps and compare generated outputs to recover the exact seed.

## Method
- Simulate the seeding process with candidate timestamps.
- Generate outputs and compare to the observed output.
- Select the timestamp that produces the matching output.

## Detailed Walkthrough
This challenge cracks an MT19937 seed when it is derived from a timestamp. If you know roughly when the seed was generated, you can brute force the small time window.

The attack tests candidate seeds until the generated output matches the observed value.

- Assume a reasonable time window for the seed.
- Generate MT19937 outputs for each candidate.
- Stop when the output matches the target.

## Implementation Notes
Scripts: crack_mt19937_seed.py
Data files: none
Run: python scripts/run_challenge.py 22

## Verification
The script prints the recovered seed and confirms it by regenerating output.
