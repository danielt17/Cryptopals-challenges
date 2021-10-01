# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 13:28:43 2021

@author: danie
"""

# https://cryptopals.com/sets/4/challenges/26

# %% Imports

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Cipher.AES import block_size
from Q32 import aes_ctr

# %% Functions

class AESCTROracle:
    def __init__(self):
        self.key = get_random_bytes(AES.block_size)
        self.nonce = 0
        self.prefix = "comment1=cooking%20MCs;userdata="
        self.suffix = ";comment2=%20like%20a%20pound%20of%20bacon"
        
    def encrypt(self,inputText):
        inputTextClean = inputText.replace(";","").replace("=","")
        plainText = (self.prefix + inputTextClean + self.suffix).encode()
        cipherText = aes_ctr(plainText,self.key,self.nonce)
        return cipherText
    
    def decrypt(self,cipherText):
        return aes_ctr(cipherText,self.key,self.nonce)
    
    def decrypt_and_cheak_admin(self,cipherText):
        plainText = aes_ctr(cipherText,self.key,self.nonce)
        return b";admin=true;" in plainText


def detect_prefix_len(Oracle,block_size):
    cipherTextClean = Oracle.encrypt('')
    cipherTextForced =  Oracle.encrypt('A')
    j = 0
    while cipherTextClean[:(j+1)*block_size] == cipherTextForced[:(j+1)*block_size]:
        j = j + 1
    curBlock = 1; prevBlock = 0; i = 0
    while curBlock != prevBlock:
        prevBlock = curBlock
        curBlock = Oracle.encrypt('A'*(i+1))[j*block_size:(j+1)*block_size]
        i = i + 1
    return j * block_size + (block_size - i) + 1

def cbc_bit_flipping(Oracle,prefix_len):
    initialText = "?admin?true"
    cipherText = Oracle.encrypt(initialText)
    semicolon = bytes([cipherText[prefix_len] ^ ord('?') ^ ord(';')]) # xor to return to 0 than xor with what we want
    equals = bytes([cipherText[prefix_len+6] ^ ord('?') ^ ord('=')])
    bitFlippedCipherText = cipherText[:prefix_len] + semicolon + cipherText[prefix_len+1:prefix_len+6] + equals + cipherText[prefix_len+7:]
    print('Request sent: (as interpented at reciver side)' + str(Oracle.decrypt(bitFlippedCipherText)))
    return Oracle.decrypt_and_cheak_admin(bitFlippedCipherText)
    
# %% Main

if __name__ == '__main__':
    Oracle = AESCTROracle();
    if Oracle.decrypt_and_cheak_admin(Oracle.encrypt(";admin=true;")) == True:
        print('Please rewrite the function the implementation is incorrect')
    else:
        print('Good implementation, have fun attacking it')
    prefix_len = detect_prefix_len(Oracle,block_size)
    print('Actual prefix length: ' + str(len(Oracle.prefix)) + '. Estimated prefix length: ' + str(prefix_len))
    print('Running cbc bit flipping to get admin priviliges:')
    if cbc_bit_flipping(Oracle,prefix_len):
        print('Gained admin priviliges')
    else:
        print('Failed to get admin priviliges')
    
    
