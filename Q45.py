# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 14:38:35 2021

@author: danie
"""

# https://cryptopals.com/sets/4/challenges/29

# %% Imports

from Q44 import SHA1_MAC, SHA1
import struct
from Crypto.Random import get_random_bytes
import numpy as np
from binascii import unhexlify

# %% Functions

class SHA1MACOracle:
    
    def __init__(self):
        self.key = get_random_bytes(np.random.randint(256))
    
    def hash_(self,message):
        return SHA1_MAC(self.key,message)
    
    def cheak_hash(self,message,hashedMessage):
        return self.hash_(message) == hashedMessage
        
def md_padding(message):
    ml = len(message) * 8 # in bits
    message = message + bytes([0x80])
    while ((len(message) * 8) % 512) != 448:
        message = message + bytes([0x00])
    message = message + struct.pack('>Q', ml)
    return message

def length_extension_attack(Oracle,originalMessage,originalHash,additionalMessage):
    hh = struct.unpack('>5I', unhexlify(originalHash)) # 5 - 32 bit blocks
    for keyLength in range(256):
        # start doesnt matter (key will be here instead)
        curMessage = md_padding(b'A' * keyLength + originalMessage)[keyLength:] + additionalMessage
        # intialize hash using the original hash, add additional message, and get the full message length
        curLen = (keyLength + len(curMessage)) * 8
        curHash = SHA1(additionalMessage, curLen, hh[0], hh[1], hh[2], hh[3], hh[4])
        if Oracle.cheak_hash(curMessage,curHash):
            return curMessage,curHash
    
    raise Exception('Length extension attack failed :( please cheak your implementation.')
        
# %% Main

if __name__ == '__main__':
    print('Length extension attack against SHA1 hash function')
    originalMessage = b"comment1=cooking%20MCs;userdata=foo;comment2=%20like%20a%20pound%20of%20bacon"
    additionalMessage = b";admin=true"
    Oracle = SHA1MACOracle()
    originalHash = Oracle.hash_(originalMessage)
    forgedMessage, forgedHash = length_extension_attack(Oracle,originalMessage,originalHash,additionalMessage)
    if additionalMessage in forgedMessage:
        print('Additional message is inside forged message')
        if Oracle.cheak_hash(forgedMessage,forgedHash):
            print('Forged hash matches forged message hash')
        else:
            print('Hashes are not matching')
    else:
        print('Additional message isnt inside forged message')
    


