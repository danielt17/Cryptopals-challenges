# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 17:25:41 2021

@author: danie
"""


# https://cryptopals.com/sets/3/challenges/24

# %% Imports

from Q35 import MT19937MersenneTwisterRNG as MT19937
import numpy as np
from Crypto.Random import get_random_bytes
import struct
from Q22 import xor
from tqdm import tqdm

# %% Functions
    
class MT19937StreamCipher:
    
    def __init__(self,seed):
        self.seed = seed
        self.rng = MT19937(seed)
        self.keyStream = b''
    
    def generate_key_stream(self,lenPlainText):
        while len(self.keyStream) < lenPlainText:
           self.keyStream = self.keyStream + struct.pack('>Q', self.rng.extract_number())
        return self.keyStream
        
    def encrypt(self,plainText):
        return xor(self.generate_key_stream(len(plainText)),plainText)
    
    def decrypt(self,cipherText):
        plainText = xor(self.keyStream,cipherText)
        return plainText

# brute force all seeds and fine in which case we find our planted text
def brute_force_mt19937_stream_cipher_seed(cipherText,knownText):
    for curSeed in tqdm(range(2**16)):
        CurOracle = MT19937StreamCipher(curSeed)
        if knownText in CurOracle.encrypt(cipherText):
            break
    return curSeed
    
# %% Main

if __name__ == '__main__': 
    prefix = get_random_bytes(np.random.randint(100)) + b';' # (k-v parsing structure)
    knownText = b'A'*14 + b';'
    suffix = b'password_reset_token=true'
    plainText = prefix + knownText + suffix
    seed = np.random.randint(2**16)
    Oracle = MT19937StreamCipher(seed)
    originalSeed = Oracle.seed
    print('\n')
    print('Original seed: ' + str(originalSeed))
    cipherText = Oracle.encrypt(plainText)
    originalKeyStream = Oracle.keyStream
    print('\n')
    print('Testing MT19937 Stream cipher oracle work correctly')
    print('\n')
    if Oracle.decrypt(cipherText) == plainText:
        print('Oracle works as intended')
    else:
        print('Please fix the oracle')
    print('\n')
    print('Brute force initiale seed of MT19937 keystream generator:')
    print('\n')
    estimatedSeed = brute_force_mt19937_stream_cipher_seed(cipherText,knownText)
    print('\n')
    if estimatedSeed == originalSeed:
        print('Successful brute force. Brute force estimated seed: ' + str(estimatedSeed))
    else:
        print('Brute force failed')
    estimatedOracle = MT19937StreamCipher(estimatedSeed); 
    print('\n')
    print('Decrypted text: ' + str(estimatedOracle.encrypt(cipherText)))
        
    
    
    
    