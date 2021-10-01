# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 16:03:31 2021

@author: danie
"""


# https://cryptopals.com/sets/4/challenges/27

# %% Imports

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Cipher.AES import block_size
from Q28 import aes_cbc_encrypt,aes_cbc_decrypt
from Q22 import xor

# %% Functions

def ascii_compliance(plainText):
    return any(curByte > 128 for curByte in plainText)
    
class AESCBCIvEqualKeyOracle:
    def __init__(self):
        self.key = get_random_bytes(AES.block_size)
        self.iv = self.key
        self.prefix = "comment1=cooking%20MCs;userdata="
        self.suffix = ";comment2=%20like%20a%20pound%20of%20bacon"
        
    def encrypt(self,inputText):
        inputTextClean = inputText.replace(";","").replace("=","")
        plainText = (self.prefix + inputTextClean + self.suffix).encode()
        cipherText = aes_cbc_encrypt(plainText,self.key,self.iv)
        return cipherText
    
    def decrypt(self,cipherText):
        return aes_cbc_decrypt(cipherText,self.key,self.iv)
    
    def decrypt_and_cheak_admin(self,cipherText):
        plainText = aes_cbc_decrypt(cipherText,self.key,self.iv)
        if ascii_compliance(plainText):
            raise Exception('The decrypted message is noncompliant',plainText)
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

def recover_key(Oracle,prefix_len):
    padAtStart = (block_size - prefix_len) % block_size
    totalLen = prefix_len + padAtStart
    padStartToFullBlock = padAtStart * '0'
    P1 = 'A' * 16; P2 = 'B' * 16; P3 = 'C' * 16 
    plainText = padStartToFullBlock + P1 + P2 + P3
    cipherText = Oracle.encrypt(plainText)
    C1 = cipherText[totalLen:(totalLen + block_size)];
    craftedCipherText = C1 + bytes([0]*16) + C1 + cipherText[-2*block_size:]  # ciphertext to make sure valid padding
    try:
        Oracle.decrypt_and_cheak_admin(craftedCipherText)
    except Exception as e:
        print(e.args[0])
        craftedPlainText = e.args[1]
    estimatedKey = xor(craftedPlainText[:block_size],craftedPlainText[(2*block_size):(3*block_size)])
    return estimatedKey
    
    

# %% Main

if __name__ == '__main__':
    Oracle = AESCBCIvEqualKeyOracle();
    if Oracle.decrypt_and_cheak_admin(Oracle.encrypt(";admin=true;")) == True:
        print('Please rewrite the function the implementation is incorrect')
    else:
        print('Good implementation, have fun attacking it')
    prefix_len = detect_prefix_len(Oracle,block_size)
    print('Actual prefix length: ' + str(len(Oracle.prefix)) + '. Estimated prefix length: ' + str(prefix_len))
    print('Estimating key:')
    estimatedKey = recover_key(Oracle,prefix_len)
    if estimatedKey == Oracle.key:
        print('Key recovered successfully!')
    else:
        print('Key recovery failed !')
    