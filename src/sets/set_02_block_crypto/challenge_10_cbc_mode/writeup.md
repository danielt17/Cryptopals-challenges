# Challenge 10: Implement CBC mode
Set: 02 - Block crypto
Cryptopals: https://cryptopals.com/sets/2/challenges/10
Run: `python scripts/run_challenge.py 10`

## Goal
Implement AES-CBC encryption and decryption using AES-ECB as the block primitive.

## Cryptographic Insight
CBC chains blocks by XORing each plaintext block with the previous ciphertext block (or IV) before encryption. Decryption reverses this by decrypting then XORing with the previous ciphertext block.

## Method
- Pad the plaintext to the AES block size.
- For each block: XOR with previous ciphertext (or IV) and encrypt with AES-ECB.
- For decryption: decrypt each block and XOR with previous ciphertext (or IV).

## Detailed Walkthrough
Implementing [CBC mode](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_block_chaining_(CBC)) is a straight forward proces but one should first understand the need for it. In ECB mode we could only encrypt regular sized messages, although padding allows us to deal with variable length message. This isn't the main problem CBC comes to deal with, we want the same blocks to be encrypted into different ciphertexts, this negates frequency analysis techniques on single blocks. This allows us to make collisions (two encryption process have the same result) extremely unlikely around 2^-64 unlikely. This is achieved using the following construction, where each encryption dependents on the previous encryption process, to start the process we have to use a unique initializaion vector (IV) which is sent over a public channel (as it is for single use, otherwise we can exploit this). The mathmatical operation and diagrams describing the mode of opeartion can be seen below.

![image](https://user-images.githubusercontent.com/60748408/154333638-8bf15ec7-8e2a-421e-9b4d-edd3b0a5d448.png)

![image](https://user-images.githubusercontent.com/60748408/154333947-4b242f9a-c435-4d61-90de-153638a97284.png)
![image](https://user-images.githubusercontent.com/60748408/154334006-c65c2ffa-6050-4e1a-ab70-6ad5d1b1d6fe.png)

In the following image which we have used before, we can see the difference between encrypting using ECB mode and CBC (or other modes) of encryption.

![image](https://user-images.githubusercontent.com/60748408/154333678-1b6ab661-26e7-4712-a3e4-ed0a56382620.png)

CBC mode chains blocks so each plaintext block is XORed with the previous ciphertext block before encryption. Decryption reverses the process by AES-decrypting and XORing with the previous ciphertext (or IV for the first block).

The implementation uses AES-ECB as the underlying primitive. Correct handling of IV, padding, and block boundaries is crucial.

- XOR plaintext block with previous ciphertext (or IV).
- Encrypt with AES-ECB to produce the next block.
- Decrypt and XOR to recover plaintext.

## Implementation Notes
Scripts: cbc_mode.py
Data files: 22.txt
Run: python scripts/run_challenge.py 10

## Verification
The script decrypts the provided ciphertext and verifies the encrypt-decrypt round trip.

Expected output (abridged):
```text
Decrypted text: 

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
...
```
