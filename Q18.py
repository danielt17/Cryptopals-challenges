# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 15:31:19 2021

@author: danie
"""


# %% Challange

# https://cryptopals.com/sets/1/challenges/8

# %% Imports

import numpy as np

# %% Functions

def detect_aes_ecb(test):
    detect = 0
    for i in range(16):
        for j in range(16):
            if i == j:
                continue
            else:
                if test[i*8:(i+1)*8] == test[j*8:(j+1)*8]:
                    detect = 1
    return detect

# %% Main

if __name__ == '__main__':
    with open('18.txt') as f:
        cypherText = bytes.fromhex(f.read())
    fullEncryptionBlock = 128; blockAmount = 16; textLen = len(cypherText)
    cypherTexts = []; detectAES = []
    for i in range(textLen//fullEncryptionBlock):
        cypherTexts.append(cypherText[i*fullEncryptionBlock:(i+1)*fullEncryptionBlock])
    for i in range(len(cypherTexts)):
        detectAES.append(detect_aes_ecb(cypherTexts[i]))
    detectAES = np.array(detectAES)
    numberOfAESECBtext = np.where(detectAES==1)[0][0]
    print('AES ECB encrypted file: ' + str(numberOfAESECBtext))
    
        