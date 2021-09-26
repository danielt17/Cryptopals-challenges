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

def create_forced_previous_block(iv, guessedByte, paddingLen, plainTextBlock):
    indexOfForcedChar = len(iv) - paddingLen
    forcedCharacter = iv[indexOfForcedChar] ^ guessedByte ^ paddingLen
    output = iv[:indexOfForcedChar] + bytes([forcedCharacter])
    m = 0
    for k in range(block_size - paddingLen + 1, block_size):
        forcedCharacter = iv[k] ^ plainTextBlock[m] ^ paddingLen
        output += bytes([forcedCharacter])
        m += 1
    return output

def cbc_padding_oracle_attack(Oracle,cipherText,iv):
    plainText = b''
    cipherTextBlocks = [iv] + [cipherText[i:i + block_size] for i in range(0, len(cipherText), block_size)]
    for c in range(1, len(cipherTextBlocks)):
        plainTextBlock = b''   
        for i in range(block_size - 1, -1, -1):
            paddingLen = len(plainTextBlock) + 1
            possibleLastBytes = []
            for j in range(256):
                forcedIv = create_forced_previous_block(cipherTextBlocks[c - 1], j, paddingLen, plainTextBlock)
                if Oracle.decrypt_oracle(cipherTextBlocks[c], forcedIv) is True:
                    possibleLastBytes += bytes([j])
            # in case something random happens (false positive with regard to padding)
            if len(possibleLastBytes) != 1:
                for byte in possibleLastBytes:
                    for j in range(256):
                        forcedIv = create_forced_previous_block(cipherTextBlocks[c - 1], j, paddingLen + 1,bytes([byte]) + plainTextBlock)
                        if Oracle.decrypt_oracle(cipherTextBlocks[c], forcedIv) is True:
                            possibleLastBytes = [byte]
                            break
            plainTextBlock = bytes([possibleLastBytes[0]]) + plainTextBlock
            print('Current progress: ' + str(plainText + plainTextBlock))
        plainText += plainTextBlock
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
    print('\n')
    print('Decrypted cipher text: ' + str(Oracle.decrypt(cipherText)) + ' . Padding oracle attack decryption: ' + str(plainText))
    print('\n')
        
    