# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 14:46:11 2021

@author: danie
"""

# %% Challange

# https://cryptopals.com/sets/1/challenges/1

# %%

from base64 import b64encode

# %% Functions

def Hex2Bytes(string):
    stringbyte = bytearray.fromhex(string)
    return stringbyte

def encodeb64(stringbyte):
    stringb64 = b64encode(stringbyte)
    return stringb64

def b64toString(stringb64):
    stringStrb64 = str(stringb64)[2:-1]
    return stringStrb64

def byteToclearb64String(stringbyte):
    stringStrb64 = b64toString(encodeb64(stringbyte))
    return stringStrb64

# %% Main

if __name__ == '__main__':
    string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    stringbyte = Hex2Bytes(string)
    stringStrb64 = byteToclearb64String(stringbyte)
    # stringb64 = encodeb64(stringbyte)
    # stringStrb64 = b64toString(stringb64)
    
    solution = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    
    if solution == stringStrb64:
        print('solved')
    else:
        print('wrong')
