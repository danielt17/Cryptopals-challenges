# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 23:04:45 2021

@author: danie
"""

# https://cryptopals.com/sets/3/challenges/18

# %% Imports

from Crypto.Cipher import AES
from Crypto.Cipher.AES import block_size
from base64 import b64decode
import struct
from Crypto.Util.Padding import pad
from Q22 import xor

# %% Functions

# does both enrypt AND decrypt
def aes_ctr(plainText,key,nonce):
    cipherText = b''
    counter = 0
    while plainText:
        nonce_counter = struct.pack('<QQ', nonce, counter) # little endian unsigned long long
        cipher = AES.new(key,AES.MODE_ECB)
        stream = cipher.encrypt(pad(nonce_counter,block_size))
        cipherText = cipherText + xor(stream, plainText[:block_size])
        plainText = plainText[block_size:]
        counter = counter + 1
    return cipherText
    

# %% Main

if __name__ == '__main__':
    key = b'YELLOW SUBMARINE'
    nonce = 0
    cipherText = b64decode('L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==')
    plainText = aes_ctr(cipherText,key,nonce)
    print('Cipher text decryptes into: ' + str(plainText.decode()) + ' \n')
    print('Testing AES CTR mode encryption decryption cycle: \n')
    print('Test 1:')
    if aes_ctr(plainText,key,nonce) == cipherText:
        print('CTR decryption encryption decryption cycle works as intended')
    else:
        print('Your AES in CTR mode doesnt work correctly')
    
    key1 = b'Hack  me  please'
    nonce1 = 17
    plainText2 = b'No time like the present'
    print('Test 2:')
    if aes_ctr(aes_ctr(plainText2,key1,nonce1),key1,nonce1) == plainText2:
        print('CTR decryption encryption decryption cycle works as intended')
    else:
        print('Your AES in CTR mode doesnt work correctly')