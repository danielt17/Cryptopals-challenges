# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 14:07:46 2021

@author: danie
"""

# https://cryptopals.com/sets/2/challenges/16

# %% Imports

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Q23 import detect_ecb_cbc
from Crypto.Util.Padding import pad,unpad

# %% Functions

def aes_cbc_encrypt(plainText,key,iv):
    cipher = AES.new(key,AES.MODE_CBC,iv = iv)
    cipherText = cipher.encrypt(pad(plainText,AES.block_size))
    return cipherText

def aes_cbc_decrypt(cipherText,key,iv):
    cipher = AES.new(key,AES.MODE_CBC,iv = iv)
    cipherText = unpad(cipher.decrypt(cipherText),AES.block_size)
    return cipherText

class AESCBCOracle:
    def __init__(self):
        self.key = get_random_bytes(AES.block_size)
        self.iv = get_random_bytes(AES.block_size)
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
        return b";admin=true;" in plainText

def detect_mode_of_operation(Oracle):
    inputText = "0" * 128
    cipherText = Oracle.encrypt(inputText)
    if detect_ecb_cbc(cipherText) == 0:
        return 'ECB'
    else:
        return 'CBC'
    
def discover_block_size(Oracle):
    initialLen = len(Oracle.encrypt(""))
    currentLen = len(Oracle.encrypt(""))
    i = 0
    while initialLen == currentLen:
        inputText = "A"*(i+1)
        currentLen = len(Oracle.encrypt(inputText))
        i = i + 1
    return currentLen - initialLen
    
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

def cbc_bit_flipping(Oracle,block_size,prefix_len):
    initialText = "?admin?true"
    prefixToFullBlock =  (block_size - len(initialText)) % block_size
    initialText = (block_size + prefixToFullBlock) * '?' + initialText
    cipherText = Oracle.encrypt(initialText)
    semicolon = bytes([cipherText[prefix_len+prefixToFullBlock] ^ ord('?') ^ ord(';')]) # xor to return to 0 than xor with what we want
    equals = bytes([cipherText[prefix_len+prefixToFullBlock+6] ^ ord('?') ^ ord('=')])
    bitFlippedCipherText = cipherText[:prefix_len+prefixToFullBlock] + semicolon + cipherText[prefix_len+prefixToFullBlock+1:prefix_len+prefixToFullBlock+6] + equals + cipherText[prefix_len+prefixToFullBlock+7:]
    print('Request sent: ' + str(Oracle.decrypt(bitFlippedCipherText)))
    return Oracle.decrypt_and_cheak_admin(bitFlippedCipherText)
    
# %% Main

if __name__ == '__main__':
    Oracle = AESCBCOracle();
    if Oracle.decrypt_and_cheak_admin(Oracle.encrypt(";admin=true;")) == True:
        print('Please rewrite the function the implementation is incorrect')
    else:
        print('Good implementation, have fun attacking it')
    mode_of_operation = detect_mode_of_operation(Oracle)
    print('Detected mode of operation: ' + mode_of_operation)
    block_size = discover_block_size(Oracle)
    print('Actual block size: ' + str(AES.block_size) + '. Estimated block size: ' + str(block_size))
    prefix_len = detect_prefix_len(Oracle,block_size)
    print('Actual prefix length: ' + str(len(Oracle.prefix)) + '. Estimated prefix length: ' + str(prefix_len))
    print('Running cbc bit flipping to get admin priviliges:')
    if cbc_bit_flipping(Oracle,block_size,prefix_len):
        print('Gained admin priviliges')
    else:
        print('Failed to get admin priviliges')
    
    
    