# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 12:54:32 2021

@author: danie
"""

# https://cryptopals.com/sets/4/challenges/25

# %% Imports

from base64 import b64decode
from sets.set_01_basics.challenge_07_aes_ecb_mode.aes_ecb_mode import aes_ecb_decrypt
from Crypto.Random import get_random_bytes
from Crypto.Cipher.AES import block_size
from sets.set_03_block_and_stream_crypto.challenge_18_aes_ctr_mode.aes_ctr_mode import aes_ctr
from pathlib import Path

# %% Functions

def load_plain_text():
    """Load plain text."""
    with Path(__file__).with_name('41.txt').open('r', encoding='utf-8') as f:
        cypherText = b64decode(f.read())
    plainText = aes_ecb_decrypt(cypherText,"YELLOW SUBMARINE".encode("utf8")).decode()
    return plainText[:-4].encode()
    
class AESCTREditOracle:
    
    def __init__(self):
        """Initialize the instance."""
        self.key = get_random_bytes(block_size)  
        self.nonce = 0
    
    def encrypt(self,plainText):
        """Encrypt."""
        cipherText = aes_ctr(plainText,self.key,self.nonce)
        return cipherText
    
    def decrypt(self,cipherText):
        """Decrypt."""
        plainText = aes_ctr(cipherText,self.key,self.nonce)
        return plainText
    
    def edit(self,cipherText,offset,newText):
        """Edit."""
        plainText = self.decrypt(cipherText)
        return self.encrypt(plainText[:offset] + newText + plainText[offset:])
        
def break_aes_ctr_random_access_read_write(cipherText,Oracle):
    # works because encryption and decryption are the same in CTR mode, 
    # therefore the start is the same up to where the original text starts
    """Break aes ctr random access read write."""
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
    
        
