# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 21:17:37 2021

@author: danie
"""

# https://cryptopals.com/sets/2/challenges/12

# %% Imports

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Q22 import aes_ecb_encrypt_padded
from Q23 import detect_ecb_cbc
from base64 import b64decode
import numpy as np

# %% Functions

class AESECBOracle:
    def __init__(self):
        self.key = get_random_bytes(AES.block_size)
        self.randomPrefix = get_random_bytes(np.random.randint(5,100))
        
    def encrypt(self,input_text,unknown_string):
        plainText = self.randomPrefix + input_text + unknown_string
        cipherText = aes_ecb_encrypt_padded(plainText,self.key)
        return cipherText


def discover_block_size(unknown_string,Oracle):
    # find what is the jump in size between encryptions with respect to input length
    # the first time there is a change in output size we get to know what in the block size.
    initialLen = len(Oracle.encrypt(b"",unknown_string))
    currentLen = len(Oracle.encrypt(b"",unknown_string))
    i = 0
    while initialLen == currentLen:
        input_text = b"A"*(i+1)
        currentLen = len(Oracle.encrypt(input_text,unknown_string))
        i = i + 1
    return currentLen - initialLen

def detect_mode_of_operation(unknown_string,Oracle):
    # crafting constant input to check if ecb or cbc like in the previous challenge 
    input_text = b"0" * 128
    cipherText = Oracle.encrypt(input_text,unknown_string)
    if detect_ecb_cbc(cipherText) == 0:
        return 'ECB'
    else:
        return 'CBC'
    
def detect_random_prefix_len(unknown_string,Oracle):
    # find with respect to block the end of the prefix, afterward search inside the block for the ending of the prefix
    cipherTextClean = Oracle.encrypt(b'',unknown_string)
    cipherTextForced =  Oracle.encrypt(b'A',unknown_string)
    j = 0
    while cipherTextClean[:(j+1)*AES.block_size] == cipherTextForced[:(j+1)*AES.block_size]:
        j = j + 1
    curBlock = 1; prevBlock = 0; i = 0
    while curBlock != prevBlock:
        prevBlock = curBlock
        curBlock = Oracle.encrypt(b'A'*(i+1),unknown_string)[j*AES.block_size:(j+1)*AES.block_size]
        i = i + 1
    return j * AES.block_size + (AES.block_size - i) + 1

def craft_one_byte_short_input(blockSize,lenDecryptedText,randomPrefixLength):
    # shift with respect to current block and how far we decrypted
    return b'A'*((blockSize - randomPrefixLength -1-lenDecryptedText) % blockSize)

def crack_one_byte_ecb(unknown_string,blockSize,decryptedText,randomPrefixLength,Oracle):
    # comparison to dictionary
    lenDecryptedText = len(decryptedText)
    oneByteShort = craft_one_byte_short_input(blockSize,lenDecryptedText,randomPrefixLength)
    cipherText = Oracle.encrypt(oneByteShort,unknown_string)
    crackLen = randomPrefixLength + len(oneByteShort) + lenDecryptedText + 1
    for i in range(256):
        pair = Oracle.encrypt(oneByteShort + decryptedText + bytes([i]),unknown_string)
        if pair[:crackLen] == cipherText[:crackLen]:
            return bytes([i])
    return b'' # to make sure we dont return a non type, could be empty due to padding

def cheackValidPadding(textpadded):
    padding_value = textpadded[-1]
    if (len(textpadded[:-textpadded[-1]]) + padding_value) == len(textpadded):
        return True
    else:
        False

def unpadding_without_blocksize(textpadded):
    if cheackValidPadding(textpadded):
        return textpadded[:-textpadded[-1]]
    else:
        print('Invalid padding')

def byte_at_a_time_ecb(unknown_string,blockSize,randomPrefixLength,Oracle):
    # one byte at a time attack on aes-ecb oracle
    cipherTextLen = len(Oracle.encrypt(b"",unknown_string)) - randomPrefixLength
    decryptedText = b""
    for i in range(cipherTextLen):
        decryptedText = decryptedText + crack_one_byte_ecb(unknown_string,blockSize,decryptedText,randomPrefixLength,Oracle)
        # print('Iteration: ' + str(i+1) + '. ' + str(decryptedText) + ' \n')
    return unpadding_without_blocksize(decryptedText)
    


# %% Main

if __name__ == '__main__':
    unknown_string = b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')
    Oracle = AESECBOracle()
    print('What we expect to get at the end: \n \n' + str(unknown_string.decode()) + '\n')
    print('\n')
    print('Analysing cipher: \n')
    blockSize = discover_block_size(unknown_string,Oracle)
    print('Detected block size of: ' + str(blockSize) + '\n')
    modeOfOperation = detect_mode_of_operation(unknown_string,Oracle)
    print('Detected mode of operation: ' + modeOfOperation + '\n')
    randomPrefixLength = detect_random_prefix_len(unknown_string,Oracle)
    print('Actual random prefix length: ' + str(len(Oracle.randomPrefix)) + '. Estimated random prefix length: ' + str(randomPrefixLength) + '\n')
    decryptedText = byte_at_a_time_ecb(unknown_string,blockSize,randomPrefixLength,Oracle)
    print('Decrypted text: ' + str(decryptedText.decode()))