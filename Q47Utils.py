# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 19:39:28 2021

@author: danie
"""


# https://cryptopals.com/sets/4/challenges/31

# %% Imports

from Q44 import SHA1
import struct
from Crypto.Random import get_random_bytes
import numpy as np
from binascii import unhexlify
from Q22 import xor
from time import sleep,time

# %% Functions

# from wikipedia https://en.wikipedia.org/wiki/HMAC

def HMAC_SHA1(key,message):
    blockSize = 64 # Bytes
    if len(key) > blockSize:
        key = unhexlify(SHA1(key))
    if len(key) < blockSize:
        key = key + bytes([0x00]) * (blockSize - len(key))
    oKeyPad = xor(key,(blockSize*bytes([0x5c])))
    iKeyPad = xor(key,(blockSize*bytes([0x36])))
    return SHA1(oKeyPad + unhexlify(SHA1(iKeyPad + message)))

def test_hmac_sha1():
    key = b"key"
    message = b"The quick brown fox jumps over the lazy dog"
    if HMAC_SHA1(key,message) == 'de7c9b85b8b78aa6bc8a7a36f70a90701c9db4d9':
        print('HMAC SHA1 implemented correctly')
    else:
        print('Please fix your HMAC-SHA1 implementation')

def insecure_compare(seq1,seq2,sleepTime):
    for bit1, bit2 in zip(seq1,seq2):
        if bit1 != bit2:
            return False
        sleep(sleepTime)
    return True

def insecure_compare_test_time():
    sleepTime = 0.05 # 50 ms
    seq1 = b'A'*20
    seq2 = b'A' + b'B'*19
    start = time()
    insecure_compare(seq1,seq1,sleepTime)
    end = time()
    print('Expected time: 1 [sec]. Actual time: ' + str(end - start))
    start = time()
    insecure_compare(seq1,seq2,sleepTime)
    end = time()
    print('Expected time: 0.05 [sec]. Actual time: ' + str(end - start))

# %% Main

if __name__ == '__main__':
    test_hmac_sha1()
    insecure_compare_test_time()
    