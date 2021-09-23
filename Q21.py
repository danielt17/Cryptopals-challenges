# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 15:57:50 2021

@author: danie
"""


# %% Challange

# https://cryptopals.com/sets/2/challenges/9

# %% Imports

from Crypto.Util.Padding import pad

# %% Functions

def PKCS7padding(text,blockSize):
    textpadded = pad(text,blockSize)
    return textpadded

# %% Main

if __name__ == '__main__':
    text = "YELLOW SUBMARINE".encode("utf8")
    textPadded = PKCS7padding(text,20)
    solution = b"YELLOW SUBMARINE\x04\x04\x04\x04"
    if textPadded == solution:
        print('Correct solution \n')
        print('Original text: ' + str(text) + '. Padded text: ' + str(textPadded))
    else:
        print('Please fix')
    