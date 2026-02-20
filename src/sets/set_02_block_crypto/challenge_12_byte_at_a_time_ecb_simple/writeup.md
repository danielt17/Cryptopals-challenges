# Challenge 12: Byte-at-a-time ECB decryption (simple)
Set: 02 - Block crypto
Cryptopals: https://cryptopals.com/sets/2/challenges/12
Run: `python scripts/run_challenge.py 12`

## Goal
Recover an unknown suffix from an ECB oracle by decrypting one byte at a time.

## Cryptographic Insight
ECB is deterministic per block. If you can align the unknown suffix so that only one byte differs, you can build a dictionary of ciphertext blocks for each candidate byte and recover the unknown suffix iteratively.

## Method
- Discover the block size by observing ciphertext length changes.
- Confirm ECB by detecting repeated blocks.
- For each position, craft input to align the next unknown byte at block end and brute force the byte via a block dictionary.

## Detailed Walkthrough
This challenge gives us our first modern cryptanalysis challenge, in which we do a Byte-at-a-time ECB decryption. The challenge teaches us how to carry out a full attack from start to finish. In the challenge we have an Oracle (A complicated way of saying we have a function which described an interaction with the encryption/decryption algorithm) where we can input a string of our own which will be concatenated by an unknown string to the user and then encrypted using AES-ECB mode, or in a more formal language: AES-128-ECB(your-string || unknown-string, random-key) which we call from now on O('your-string').

1. We start by figuring out the block size of our encryption function. We start by calling the oracle in the following way Oracle(''), we get the current out length of the ciphertext, which we call initial length (n). Now we start querying the oracle in the following way Oracle('A'* i) we search for the first value of i for which the length of the ciphertext changes, we call this value current length (m). By subtracting m-n we get the block size of the cipher.
2. Now we detect the mode of operation, as we have done in Challenge 11 (we input constant '0'* 128 so we will find repeating blocks).
3. Finally we get into constructing our query method, we will look at the simple case of zero known bytes as it is easy to generalize the procedure from here. Lets query the Oracle using the following method O('A'* ((blockSize-1) % blockSize)) (adding lenDecryptedText generalizes the method), we get that the first byte of the unknown string enters a block of (blockSize-1) known bytes. We can exploit this by taking this resulting ciphertext and define an oracle O('A'* ((blockSize-1) % blockSize) + i) such that we go over 256 possible values for i, and when we find i such that the new ciphertext equals the previous ciphertext we have hit jackpot. This procedure can be generalized to any length we want, and we have recovered the unknown string in linear time.

Byte-at-a-time ECB decryption exploits ECB determinism to recover an unknown suffix. By carefully choosing the input length, the next unknown byte can be aligned at the end of a block and guessed by building a dictionary of all possible last-byte values.

The attack repeats this for each position. It also measures the block size and verifies that the oracle uses ECB before proceeding.

- Detect the block size by measuring ciphertext length changes.
- Confirm ECB mode using repeated blocks.
- Build a dictionary for each byte and recover the suffix iteratively.

## Implementation Notes
Scripts: byte_at_a_time_ecb_simple.py
Data files: none
Run: python scripts/run_challenge.py 12

## Verification
The script prints the recovered plaintext and intermediate iterations.

Expected output (abridged):
```text
What we expect to get at the end: 
 
Rollin' in my 5.0
With my rag-top down so my hair can blow
The girlies on standby waving just to say hi
Did you stop? No, I just drove by




Analysing cipher: 

Detected block size of: 16

Detected mode of operation: ECB

Iteration: 1. b'R' 

Iteration: 2. b'Ro' 

Iteration: 3. b'Rol' 

Iteration: 4. b'Roll' 

Iteration: 5. b'Rolli' 

Iteration: 6. b'Rollin' 

Iteration: 7. b"Rollin'" 

Iteration: 8. b"Rollin' " 

Iteration: 9. b"Rollin' i" 

Iteration: 10. b"Rollin' in" 

Iteration: 11. b"Rollin' in " 

Iteration: 12. b"Rollin' in m" 

...
```
