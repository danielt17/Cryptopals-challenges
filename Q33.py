# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 12:45:38 2021

@author: danie
"""

# https://cryptopals.com/sets/3/challenges/19

# %% Imports

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Cipher.AES import block_size
from base64 import b64decode
from Q32 import aes_ctr
from Q22 import xor
import numpy as np

# %% Functions

class AESCTRFixedNonceOracle:
    
    def __init__(self):
        self.key = get_random_bytes(AES.block_size) 
        self.nonce = 0
    
    def encrypt(self,plainText):
        cipherText = aes_ctr(plainText,self.key,self.nonce)
        return cipherText
    
    def decrypt(self,cipherText):
        plainText = aes_ctr(cipherText,self.key,self.nonce)
        return plainText

def load_plain_texts():
    lines = []
    with open('33.txt') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = b64decode(lines[i])
    return lines

def encrypt_plaintexts(Oracle,plainTexts):
    cipherTexts = []
    for i in range(len(plainTexts)):
        cipherTexts.append(Oracle.encrypt(plainTexts[i]))
    return cipherTexts

def get_ciphertexts_lengths(cipherTexts):
    lenCipherTexts = []
    for i in range(len(cipherTexts)):
        lenCipherTexts.append(len(cipherTexts[i]))
    return lenCipherTexts

def get_english_score(input_bytes):
    CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
    }
    score = 0
    for byte in input_bytes:
        score += CHARACTER_FREQ.get(chr(byte).lower(), 0)
    return score

# this code can be improved by a better english score method 

def attack_ctr_using_substitutions(cipherTexts):
    lenCipherTexts = get_ciphertexts_lengths(cipherTexts)
    maxLength = max(lenCipherTexts)
    streamCipherRecovered = [0] * maxLength
    for curByte in range(maxLength):
        score = [0]*256
        for curKeyByteValue in range(256):
            streamCipherRecovered[curByte] = curKeyByteValue
            for ind,curCipherText in enumerate(cipherTexts):
                maxIndex = min(curByte+1,lenCipherTexts[ind])
                curXor = xor(curCipherText[:maxIndex],bytes(streamCipherRecovered[:maxIndex]))
                score[curKeyByteValue] = score[curKeyByteValue] + get_english_score(curXor)
        streamCipherRecovered[curByte] = np.argmax(np.array(score))
        print(xor(curCipherText[:curByte+1],bytes(streamCipherRecovered[:curByte+1])))
    return bytes(streamCipherRecovered)
            
def reconstruct_plaintexts(cipherTexts,recoveredStreamCipher):
    plainTexts = []
    for i in range(len(cipherTexts)):
        plainTexts.append(xor(cipherTexts[i],recoveredStreamCipher).decode())
        
    return plainTexts
        
def comparison_one_by_one(plainTexts,recoveredPlainTexts):
    print('\n')
    print('Comparing recovery results: \n')
    for i in range(len(plainTexts)):
        print('Original plaintext: ' + str(plainTexts[i]) + '. Recovered plaintext: ' + str(recoveredPlainTexts[i]))
        
# %% Main

if __name__ == '__main__':
    Oracle = AESCTRFixedNonceOracle()
    print('AES CTR mode key: ' + str(Oracle.key))
    plainTexts = load_plain_texts()
    cipherTexts = encrypt_plaintexts(Oracle,plainTexts)
    recoveredStreamCipher = attack_ctr_using_substitutions(cipherTexts)
    print('Recovered stream cipher: ' + str(recoveredStreamCipher))
    recoveredPlainTexts = reconstruct_plaintexts(cipherTexts,recoveredStreamCipher)
    comparison_one_by_one(plainTexts,recoveredPlainTexts)
    