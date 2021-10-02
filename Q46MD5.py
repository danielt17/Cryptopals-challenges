# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 16:37:29 2021

@author: danie
"""


# https://cryptopals.com/sets/4/challenges/30 - MD5 version (instead of MD4)

# %% Imports

import struct
from Crypto.Random import get_random_bytes
import numpy as np
from binascii import unhexlify,hexlify
import math

# %% Functions


# MD5 implementation taken from https://github.com/FiloSottile/crypto.py/blob/master/3/md5.py
lrot = lambda x, n: (x << n) | (x >> (32 - n))


class MD5():

    # r specifies the per-round shift amounts
    r = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
         5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
         4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
         6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

    # Use binary integer part of the sines of integers (Radians) as constants
    k = [math.floor(abs(math.sin(i + 1)) * (2 ** 32)) for i in range(64)]

    def __init__(self, message, ml=None, A = 0x67452301, B = 0xefcdab89, C = 0x98badcfe, D = 0x10325476):
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
        w = list(struct.unpack('<' + 'I' * 16, chunk))

        a, b, c, d = self.A, self.B, self.C, self.D

        for i in range(64):
            if i < 16:
                f = (b & c) | ((~b) & d)
                g = i
            elif i < 32:
                f = (d & b) | ((~d) & c)
                g = (5 * i + 1) % 16
            elif i < 48:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:
                f = c ^ (b | (~d))
                g = (7 * i) % 16

            x = b + lrot((a + f + self.k[i] + w[g]) & 0xffffffff, self.r[i])
            a, b, c, d = d, x & 0xffffffff, b, c

        self.A = (self.A + a) & 0xffffffff
        self.B = (self.B + b) & 0xffffffff
        self.C = (self.C + c) & 0xffffffff
        self.D = (self.D + d) & 0xffffffff

    def digest(self):
        return struct.pack('<IIII', self.A, self.B, self.C, self.D)

    def hexdigest(self):
        return hexlify(self.digest()).decode()

def MD5_MAC(key,message):
    return MD5(key + message).hexdigest()

class MD5Oracle:
    
    def __init__(self):
        self.key = get_random_bytes(np.random.randint(256))
    
    def hash_(self,message):
        return MD5_MAC(self.key,message)
    
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
        curHash = MD5(additionalMessage, curLen, hh[0], hh[1], hh[2], hh[3]).hexdigest()
        if Oracle.cheak_hash(curMessage,curHash):
            return curMessage,curHash
    
    raise Exception('Length extension attack failed :( please cheak your implementation.')
        
# %% Main

if __name__ == '__main__':
    print('Length extension attack against MD5 hash function')
    originalMessage = b"comment1=cooking%20MCs;userdata=foo;comment2=%20like%20a%20pound%20of%20bacon"
    additionalMessage = b";admin=true"
    Oracle = MD5Oracle()
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