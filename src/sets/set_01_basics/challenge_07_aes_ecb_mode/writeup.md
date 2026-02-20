# Challenge 07: AES in ECB mode
Set: 01 - Basics
Cryptopals: https://cryptopals.com/sets/1/challenges/7
Run: `python scripts/run_challenge.py 7`

## Goal
Decrypt an AES-ECB ciphertext with a known key.

## Cryptographic Insight
ECB mode encrypts each block independently. With a known key, decryption is straightforward block-by-block AES without any chaining or IV.

## Method
- Decode the base64 ciphertext from the input file.
- Decrypt with AES-128-ECB using the provided key.
- Strip the trailing padding and display the plaintext.

## Detailed Walkthrough
Using [AES-128](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) in [ECB mode](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_codebook_(ECB)) to decrypt the ciphertext. AES-128 is a block cipher, meaning it works on blocks of size 128 bits. ECB mode is a mode of operation of a block cipher, a 128 bit block from the plaintext is encrypted in the same way no matter where it is in text. 

<p align="center">
  <img src="https://user-images.githubusercontent.com/60748408/135771177-229ff8fa-581e-4052-a905-35249ecfd9eb.png" />
</p>

This mode operation should not be used for encryption as we will see later, an image descrbing the problematic ECB mode operation can be seen below.

<p align="center">
  <img src="https://user-images.githubusercontent.com/60748408/135771122-5163eac1-ce9d-4e47-8b13-c286a906c729.png" />
</p>

This challenge uses AES-128 in ECB mode to decrypt a base64-encoded file. ECB encrypts each 16-byte block independently, so decryption is simply block-by-block AES with the given key.

The task is mostly about correct decoding and AES usage. The typical key used in the Cryptopals challenge is "YELLOW SUBMARINE".

- Decode the base64 ciphertext.
- Decrypt with AES-128 in ECB mode.
- Output the plaintext.

## Implementation Notes
Scripts: aes_ecb_mode.py
Data files: 17.txt
Run: python scripts/run_challenge.py 7

## Verification
The script prints the decrypted text and checks a simple encryption/decryption round-trip.

Expected output (abridged):
```text
I'm back and I'm ringin' the bell 
A rockin' on the mike while the fly girls yell 
In ecstasy in the back of me 
Well that's my DJ Deshay cuttin' all them Z's 
Hittin' hard and the girlies goin' crazy 
Vanilla's on the mike, man I'm not lazy. 

I'm lettin' my drug kick in 
It controls my mouth and I begin 
To just let it flow, let my concepts go 
My posse's to the side yellin', Go Vanilla Go! 

Smooth 'cause that's the way I will be 
And if you don't give a damn, then 
Why you starin' at me 
So get off 'cause I control the stage 
There's no dissin' allowed 
I'm in my own phase 
...
```
