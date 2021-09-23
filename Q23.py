# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 22:01:25 2021

@author: danie
"""


# %% Challange

# https://cryptopals.com/sets/2/challenges/11

# %% Imports

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import numpy as np
from Q22 import aes_ecb_encrypt_padded,aes_cbc_encrypt
# %% Functions

def encryption_oracle_ecb_cbc(input_text):
    Key = get_random_bytes(AES.block_size)
    plainText = get_random_bytes(np.random.randint(5,11)) + input_text + get_random_bytes(np.random.randint(5,11))
    if np.random.randint(2) == 0:
        cipherType = 0 # ECB
        cipherText = aes_ecb_encrypt_padded(plainText,Key)
    else:
        cipherType = 1 # CBC
        Iv = get_random_bytes(AES.block_size)
        cipherText = aes_cbc_encrypt(plainText,Key,Iv)
    return cipherType,cipherText

def detect_aes_ecb_byte_version(cipherText):
    detect = 0
    chunks = [cipherText[i:i + AES.block_size] for i in range(0, len(cipherText), AES.block_size)]
    repetition = len(chunks) - len(np.unique(chunks))
    if repetition > 0:
        detect = 1 
    return detect

def detect_ecb_cbc(cipherText):
    if detect_aes_ecb_byte_version(cipherText) == 1:
        return 0
    else:
        return 1
    

# %% Main

if __name__ == '__main__':
    input_text = b"0" * 64
    success_counter = 0
    Experiments = 1000
    for i in range(Experiments):
        cipherType,cipherText = encryption_oracle_ecb_cbc(input_text)
        if cipherType == detect_ecb_cbc(cipherText):
            success_counter = success_counter + 1
    print('Experiments: ' + str(Experiments) + '. Successful: ' + str(success_counter))
    
    
    