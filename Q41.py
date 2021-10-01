# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 12:54:32 2021

@author: danie
"""

# https://cryptopals.com/sets/4/challenges/25

# %% Imports

from base64 import b64decode
from Q17 import aes_ecb_decrypt
from Crypto.Random import get_random_bytes
from Crypto.Cipher.AES import block_size
from Q32 import aes_ctr

# %% Functions

def load_plain_text():
    with open('41.txt') as f:
        cypherText = b64decode(f.read())
    plainText = aes_ecb_decrypt(cypherText,"YELLOW SUBMARINE".encode("utf8")).decode()
    return plainText[:-4].encode()
    
class AESCTREditOracle:
    
    def __init__(self):
        self.key = get_random_bytes(block_size)  
        self.nonce = 0
    
    def encrypt(self,plainText):
        cipherText = aes_ctr(plainText,self.key,self.nonce)
        return cipherText
    
    def decrypt(self,cipherText):
        plainText = aes_ctr(cipherText,self.key,self.nonce)
        return plainText
    
    def edit(self,cipherText,offset,newText):
        plainText = self.decrypt(cipherText)
        return self.encrypt(plainText[:offset] + newText + plainText[offset:])
        
def break_aes_ctr_random_access_read_write(cipherText,Oracle):
    # works because encryption and decryption are the same in CTR mode, 
    # therefore the start is the same up to where the original text starts
    plainText = Oracle.edit(cipherText,0,cipherText) 
    return plainText[:len(cipherText)]

# %% Main

if __name__ == '__main__': 
    plainText = load_plain_text()
    Oracle = AESCTREditOracle()
    cipherText = Oracle.encrypt(plainText)
    estimatedPlainText = break_aes_ctr_random_access_read_write(cipherText,Oracle)
    if estimatedPlainText == plainText:
        print('Plain text recovered succesfully !')
    else:
        print('Attack failed')
    
        