# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 13:01:44 2021

@author: danie
"""

# %% Challange

# https://cryptopals.com/sets/2/challenges/12

# %% Imports

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Q22 import aes_ecb_encrypt_padded
from Q23 import detect_ecb_cbc
from base64 import b64decode

# %% Global key variable (to make sure there is no cheating involved)

KEY = get_random_bytes(AES.block_size)

# %% Functions

def encryption_oracle_ecb(input_text,unknown_string,Key=KEY):
    # AES ECB encryption oracle with constant global key
    # dont worry there is no cheating with regards to unknown string
    plainText = input_text + unknown_string
    cipherText = aes_ecb_encrypt_padded(plainText,Key)
    return cipherText

def discover_block_size(unknown_string):
    # find what is the jump in size between encryptions with respect to input length
    # the first time there is a change in output size we get to know what in the block size.
    initialLen = len(encryption_oracle_ecb(b"",unknown_string))
    currentLen = len(encryption_oracle_ecb(b"",unknown_string))
    i = 0
    while initialLen == currentLen:
        input_text = b"A"*(i+1)
        currentLen = len(encryption_oracle_ecb(input_text,unknown_string))
        i = i + 1
    return currentLen - initialLen

def detect_mode_of_operation(unknown_string):
    # crafting constant input to check if ecb or cbc like in the previous challenge 
    input_text = b"0" * 128
    cipherText = encryption_oracle_ecb(input_text,unknown_string)
    if detect_ecb_cbc(cipherText) == 0:
        return 'ECB'
    else:
        return 'CBC'
    
def craft_one_byte_short_input(blockSize,lenDecryptedText):
    # shift with respect to current block and how far we decrypted
    return b'A'*((blockSize-1-lenDecryptedText) % blockSize)

def crack_one_byte_ecb(unknown_string,blockSize,decryptedText):
    # comparison to dictionary
    lenDecryptedText = len(decryptedText)
    oneByteShort = craft_one_byte_short_input(blockSize,lenDecryptedText)
    cipherText = encryption_oracle_ecb(oneByteShort,unknown_string)
    crackLen = len(oneByteShort) + lenDecryptedText + 1
    for i in range(256):
        pair = encryption_oracle_ecb(oneByteShort + decryptedText + bytes([i]),unknown_string)
        if pair[:crackLen] == cipherText[:crackLen]:
            return bytes([i])
    return b'' # to make sure we dont return a non type, could be empty due to padding

def byte_at_a_time_ecb(unknown_string,blockSize):
    # one byte at a time attack on aes-ecb oracle
    cipherTextLen = len(encryption_oracle_ecb(b"",unknown_string))
    decryptedText = b""
    for i in range(cipherTextLen):
        decryptedText = decryptedText + crack_one_byte_ecb(unknown_string,blockSize,decryptedText)
        print('Iteration: ' + str(i) + ' . ' + str(decryptedText) + ' \n')
    return decryptedText
    

# %% Main

if __name__ == '__main__':
    unknown_string = b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')
    print('What we expect to get at the end: \n \n' + str(unknown_string.decode()) + '\n')
    print('\n')
    print('Analysing cipher: \n')
    blockSize = discover_block_size(unknown_string)
    print('Detected block size of: ' + str(blockSize) + '\n')
    modeOfOperation = detect_mode_of_operation(unknown_string)
    print('Detected mode of operation: ' + modeOfOperation + '\n')
    print('Build dictionary')
    decryptedText = byte_at_a_time_ecb(unknown_string,blockSize)
    print('Decrypted text: ' + str(decryptedText.decode())[:-1])
