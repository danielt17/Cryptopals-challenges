# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 21:10:06 2021

@author: danie
"""


# https://cryptopals.com/sets/3/challenges/17

# %% Imports

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Q28 import aes_cbc_encrypt, aes_cbc_decrypt
import numpy as np

# %% Functions

class AESCBCPaddingOracle:
    
    def __init__(self):
        self.key = get_random_bytes(AES.block_size)
        self.iv = get_random_bytes(AES.block_size)
        self.strings = ['MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=','MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=','MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==','MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==','MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl','MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==','MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==','MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=','MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=','MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93']
    
    def encrypt(self):
        return aes_cbc_encrypt(self.strings[np.random.randint(10)].encode(),self.key,self.iv)
    
    def decrypt(self,cipherText):
        return aes_cbc_decrypt(cipherText,self.key,self.iv)
    
    def decrypt_oracle(self,cipherText):
        try:
            aes_cbc_decrypt(cipherText,self.key,self.iv)
            return True
        except ValueError:
            return False
        
def cbc_padding_oracle_attack(Oracle,cipherText,iv):
    plainText = b''
    return plainText

# %% Main

if __name__ == '__main__':
    Oracle = AESCBCPaddingOracle()
    cipherText = Oracle.encrypt()
    iv = Oracle.iv
    plainText = cbc_padding_oracle_attack(Oracle,cipherText,iv)
    print('Decrypted cipher text: ' + str(Oracle.decrypt(cipherText)) + ' . Padding oracle attack decryption: ' + str(plainText))
    
        
    