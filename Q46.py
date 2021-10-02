# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 16:15:00 2021

@author: danie
"""

# https://cryptopals.com/sets/4/challenges/30

# %% Imports

import struct
from Crypto.Random import get_random_bytes
import numpy as np
from binascii import unhexlify,hexlify

# %% Functions


# MD4 implementation taken from https://github.com/FiloSottile/crypto.py/blob/master/3/md4.py
lrot = lambda x, n: (x << n) | (x >> (32 - n))

class MD4():

    buf = [0x00] * 64

    _F = lambda self, x, y, z: ((x & y) | (~x & z))
    _G = lambda self, x, y, z: ((x & y) | (x & z) | (y & z))
    _H = lambda self, x, y, z: (x ^ y ^ z)

    def __init__(self, message,ml=None, A = 0x67452301, B = 0xefcdab89, C = 0x98badcfe, D = 0x10325476):
        self.A, self.B, self.C, self.D = A, B, C, D
        if ml is None:
            ml = len(message) * 8
        length = struct.pack('<Q',ml)
        while len(message) > 64:
            self._handle(message[:64])
            message = message[64:]
        message += b'\x80'
        message += bytes((56 - len(message) % 64) % 64)
        message += length
        while len(message):
            self._handle(message[:64])
            message = message[64:]

    def _handle(self, chunk):
        X = list(struct.unpack('<' + 'I' * 16, chunk))
        A, B, C, D = self.A, self.B, self.C, self.D

        for i in range(16):
            k = i
            if i % 4 == 0:
                A = lrot((A + self._F(B, C, D) + X[k]) & 0xffffffff, 3)
            elif i % 4 == 1:
                D = lrot((D + self._F(A, B, C) + X[k]) & 0xffffffff, 7)
            elif i % 4 == 2:
                C = lrot((C + self._F(D, A, B) + X[k]) & 0xffffffff, 11)
            elif i % 4 == 3:
                B = lrot((B + self._F(C, D, A) + X[k]) & 0xffffffff, 19)

        for i in range(16):
            k = (i // 4) + (i % 4) * 4
            if i % 4 == 0:
                A = lrot((A + self._G(B, C, D) + X[k] + 0x5a827999) & 0xffffffff, 3)
            elif i % 4 == 1:
                D = lrot((D + self._G(A, B, C) + X[k] + 0x5a827999) & 0xffffffff, 5)
            elif i % 4 == 2:
                C = lrot((C + self._G(D, A, B) + X[k] + 0x5a827999) & 0xffffffff, 9)
            elif i % 4 == 3:
                B = lrot((B + self._G(C, D, A) + X[k] + 0x5a827999) & 0xffffffff, 13)

        order = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        for i in range(16):
            k = order[i]
            if i % 4 == 0:
                A = lrot((A + self._H(B, C, D) + X[k] + 0x6ed9eba1) & 0xffffffff, 3)
            elif i % 4 == 1:
                D = lrot((D + self._H(A, B, C) + X[k] + 0x6ed9eba1) & 0xffffffff, 9)
            elif i % 4 == 2:
                C = lrot((C + self._H(D, A, B) + X[k] + 0x6ed9eba1) & 0xffffffff, 11)
            elif i % 4 == 3:
                B = lrot((B + self._H(C, D, A) + X[k] + 0x6ed9eba1) & 0xffffffff, 15)

        self.A = (self.A + A) & 0xffffffff
        self.B = (self.B + B) & 0xffffffff
        self.C = (self.C + C) & 0xffffffff
        self.D = (self.D + D) & 0xffffffff

    def digest(self):
        return struct.pack('<IIII', self.A, self.B, self.C, self.D)

    def hexdigest(self):
        return hexlify(self.digest()).decode()

def MD4_MAC(key,message):
    return MD4(key + message).hexdigest()

class MD4Oracle:
    
    def __init__(self):
        self.key = get_random_bytes(np.random.randint(256))
    
    def hash_(self,message):
        return MD4_MAC(self.key,message)
    
    def cheak_hash(self,message,hashedMessage):
        return self.hash_(message) == hashedMessage
        
def md_padding(message):
    ml = len(message) * 8 # in bits
    message += bytes([0x80])
    message += bytes((56 - len(message) % 64) % 64)
    message += struct.pack('<Q', ml)
    return message

def length_extension_attack(Oracle,originalMessage,originalHash,additionalMessage):
    hh = struct.unpack('4I', unhexlify(originalHash)) # 4 - 32 bit blocks
    for keyLength in range(256):
        # start doesnt matter (key will be here instead)
        curMessage = md_padding(b'A' * keyLength + originalMessage)[keyLength:] + additionalMessage
        # intialize hash using the original hash, add additional message, and get the full message length
        curLen = (keyLength + len(curMessage)) * 8
        curHash = MD4(additionalMessage, curLen, hh[0], hh[1], hh[2], hh[3]).hexdigest()
        if Oracle.cheak_hash(curMessage,curHash):
            return curMessage,curHash
    
    raise Exception('Length extension attack failed :( please cheak your implementation.')
        
# %% Main

if __name__ == '__main__':
    print('Length extension attack against MD4 hash function')
    originalMessage = b"comment1=cooking%20MCs;userdata=foo;comment2=%20like%20a%20pound%20of%20bacon"
    additionalMessage = b";admin=true"
    Oracle = MD4Oracle()
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
