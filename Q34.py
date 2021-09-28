# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:12:52 2021

@author: danie
"""

# https://cryptopals.com/sets/3/challenges/20

# %% Imports

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Cipher.AES import block_size
from base64 import b64decode
from Q33 import AESCTRFixedNonceOracle,encrypt_plaintexts,attack_ctr_using_substitutions,reconstruct_plaintexts,comparison_one_by_one
import numpy as np

# %% Functions

def load_plain_texts():
    lines = []
    with open('34.txt') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = b64decode(lines[i])
    return lines

# %% Main

if __name__ == '__main__':
    Oracle = AESCTRFixedNonceOracle()
    print('AES CTR mode key: ' + str(Oracle.key))
    plainTexts = load_plain_texts()
    cipherTexts = encrypt_plaintexts(Oracle,plainTexts)
    recoveredStreamCipher = attack_ctr_using_substitutions(cipherTexts)
    print('Recovered stream cipher: ' + str(recoveredStreamCipher))
    recoveredPlainTexts = reconstruct_plaintexts(cipherTexts,recoveredStreamCipher)
    comparison_one_by_one(plainTexts,recoveredPlainTexts)