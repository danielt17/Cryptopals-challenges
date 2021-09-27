# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 21:10:06 2021

@author: danie
"""


# https://cryptopals.com/sets/3/challenges/17

# %% Imports

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Cipher.AES import block_size
from Q28 import aes_cbc_encrypt, aes_cbc_decrypt
import numpy as np
from Crypto.Util.Padding import unpad

# %% Functions

class AESCBCPaddingOracle:
    
    def __init__(self):
        self.key = get_random_bytes(AES.block_size)
        self.iv = get_random_bytes(AES.block_size)
        self.strings = ['MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=','MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=','MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==','MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==','MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl','MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==','MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==','MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=','MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=','MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93']
    
    def encrypt(self):
        return aes_cbc_encrypt(self.strings[np.random.randint(10)].encode(),self.key,self.iv)
    
    def decrypt_without_padding(self,cipherText):
        cipher = AES.new(self.key,AES.MODE_CBC,iv = self.iv)
        plainText = cipher.decrypt(cipherText)
        return plainText
    
    def decrypt(self,cipherText):
        return aes_cbc_decrypt(cipherText,self.key,self.iv)
    
    def decrypt_oracle(self,cipherText,iv):
        try:
            aes_cbc_decrypt(cipherText,self.key,iv)
            return True
        except ValueError:
            return False

def cbc_padding_oracle_attack(Oracle,cipherText,iv):
    plainText = b''
    blocks = [iv]
    for i in range(len(cipherText)//block_size):
        blocks.append(cipherText[i*block_size:(i+1)*block_size])
    for i in range(len(blocks)-1):
        fakeIV = [0]*16
        blockPlainText = b''
        for padding in range(1,block_size + 1):
            for candidate in range(256):
                fakeIV[-padding] = candidate
                if Oracle.decrypt_oracle(blocks[i+1],bytes(fakeIV)):
                    blockPlainText = bytes([candidate ^ padding ^ blocks[i][-padding]]) + blockPlainText # get plainText from the bit by zeroing than xoring
            for j in range(1,padding + 1):
                fakeIV[-j] = blockPlainText[-j] ^ (padding + 1) ^ blocks[i][-j] # switch value corresponding to next element in padding
        plainText = plainText + blockPlainText
    return unpad(plainText,block_size)                
                
    
    
    

# %% Main

if __name__ == '__main__':
    Oracle = AESCBCPaddingOracle()
    cipherText = Oracle.encrypt()
    iv = Oracle.iv
    # when sending a message, there will be json containing cipherText, iv
    print('\n')
    print('Cracking starts: ')
    print('\n')
    plainText = cbc_padding_oracle_attack(Oracle,cipherText,iv)
    if Oracle.decrypt(cipherText) == plainText:
        print('Successful attack !!!')
        print('Decrypted cipher text: ' + str(Oracle.decrypt(cipherText)) + ' . Padding oracle attack decryption: ' + str(plainText))
    else:
        print('Padding oracle attack failed')
    print('\n')
        
    