# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 15:57:50 2021

@author: danie
"""


# %% Challange

# https://cryptopals.com/sets/2/challenges/9

# %% Imports

from Crypto.Util.Padding import pad, unpad

# %% Functions

def PKCS7padding(text,blockSize):
    if len(text) == blockSize:
        textpadded = text
    else:
        textpadded = pad(text,blockSize)
    return textpadded

def PKCS7unpadding(textpadded,blockSize):
    if len(textpadded) == blockSize:
        text = textpadded
    else: 
        text = unpad(textpadded, blockSize)
    return text

def PKCS7unpaddingFixed(textpadded,blockSize):
    text = unpad(textpadded, blockSize)
    return text
    
# %% Main

if __name__ == '__main__':
    text = "YELLOW SUBMARINE".encode("utf8")
    textPadded = PKCS7padding(text,20)
    solution = b"YELLOW SUBMARINE\x04\x04\x04\x04"
    if textPadded == solution:
        print('Correct solution \n')
        print('Original text: ' + str(text) + '. Padded text: ' + str(textPadded) + ' \n')
        print('Unpadded text: ' + str(PKCS7unpaddingFixed(textPadded,20)))
    else:
        print('Please fix')
    