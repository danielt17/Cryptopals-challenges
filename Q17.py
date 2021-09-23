# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 14:59:23 2021

@author: danie
"""


# %% Challange

# https://cryptopals.com/sets/1/challenges/7

# %% Imports

from base64 import b64decode
from Crypto.Cipher import AES

# %% Functions

def aes_ecb_decrypt(cypherText,Key):
    AES_ECB_cypher = AES.new(Key,AES.MODE_ECB)
    plaintext = AES_ECB_cypher.decrypt(cypherText)
    return plaintext

# %% Main

if __name__ == '__main__':
    with open('17.txt') as f:
        cypherText = b64decode(f.read())
    Key = "YELLOW SUBMARINE".encode("utf8")
    plaintext = aes_ecb_decrypt(cypherText,Key).decode()
    print(plaintext)
