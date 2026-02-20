# Challenge 20: Break fixed-nonce CTR statistically
Set: 03 - Block and stream crypto
Cryptopals: https://cryptopals.com/sets/3/challenges/20
Run: `python scripts/run_challenge.py 20`

## Goal
Break fixed-nonce CTR statistically across many ciphertexts.

## Cryptographic Insight
This is a statistical variant of the previous challenge. By aligning ciphertexts and scoring each byte position across all samples, you can recover the keystream with frequency analysis.

## Method
- Truncate ciphertexts to a common length.
- For each position, score all 256 key bytes against English frequency.
- Assemble the best-scoring keystream and decrypt.

## Detailed Walkthrough
This is the statistical variant of the fixed-nonce CTR break. The idea is the same: the keystream is reused, and each column of bytes can be treated like a single-byte XOR problem.

Statistics across many ciphertexts help resolve ambiguous bytes. A scoring function over printable ASCII and letter frequencies yields the most likely keystream byte for each column.

- Truncate ciphertexts to a common length.
- Score each key byte candidate per column.
- Assemble the keystream and decrypt.

## Implementation Notes
Scripts: break_fixed_nonce_ctr_statistical.py
Data files: 34.txt
Run: python scripts/run_challenge.py 20

## Verification
The script prints recovered plaintexts and the inferred keystream.
