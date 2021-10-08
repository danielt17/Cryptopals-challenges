# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 19:42:45 2021

@author: danie
"""


# https://cryptopals.com/sets/5/challenges/36

# %% Imports

from binascii import unhexlify
from hashlib import sha256
from Q22 import xor


# %% Functions

def HMAC_SHA256(key,message):
    blockSize = 64 # Bytes
    if len(key) > blockSize:
        key = unhexlify(sha256(key).hexdigest())
    if len(key) < blockSize:
        key = key + bytes([0x00]) * (blockSize - len(key))
    oKeyPad = xor(key,(blockSize*bytes([0x5c])))
    iKeyPad = xor(key,(blockSize*bytes([0x36])))
    return sha256(oKeyPad + unhexlify(sha256(iKeyPad + message).hexdigest())).hexdigest()
