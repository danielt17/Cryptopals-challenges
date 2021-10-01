# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 18:56:21 2021

@author: danie
"""


# https://cryptopals.com/sets/4/challenges/28

# %% Imports

import struct
import hashlib

# %% Functions

def left_rotate(value, shift):
    return ((value << shift) & 0xffffffff) | (value >> (32 - shift))

# SHA1 hash function implementation from wikipedia (0xffffffff is used to make sure things stay at 8 bytes length)
def SHA1(message, ml=None, h0=0x67452301, h1=0xEFCDAB89, h2=0x98BADCFE, h3=0x10325476, h4=0xC3D2E1F0):
    # Initialize variables:
    if ml is None:
        ml = len(message) * 8
    # Pre-processing: (always  multiple of 8 bits)
    message = message + bytes([0x80])
    while ((len(message) * 8) % 512) != 448:
        message = message + bytes([0x00])
    message = message + struct.pack('>Q', ml)
    # Process the message in successive 512-bit chunks:
    for i in range(0, len(message), 64):
        # break chunk into sixteen 32-bit big-endian words w[i], 0 ≤ i ≤ 15
        w = [0] * 80
        for j in range(16):
            w[j] = struct.unpack('>I', message[i + j * 4:i + j * 4 + 4])[0]
        # Message schedule: extend the sixteen 32-bit words into eighty 32-bit words:
        for j in range(16, 80):
            # Note 3: SHA-0 differs by not having this leftrotate.
            w[j] = left_rotate(w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16], 1)
        # Initialize hash value for this chunk:
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        # Main loop
        for j in range(80):
            if j <= 19:
                f = (b & c) | ((~ b) & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (d & (b | c))
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6
    
            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xffffffff
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp
        # Add this chunk's hash to result so far:
        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff

    # Produce the final hash value (big-endian) as a 160 bit number (hex formatted):
    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

def SHA1_MAC(key,message):
    return SHA1(key + message)

# %% Main

if __name__ == '__main__':
    print('Testing SHA1 implementation: \n')
    if '2fd4e1c67a2d28fced849ee1bb76e7391b93eb12' == SHA1(b"The quick brown fox jumps over the lazy dog"):
        print('Passed test 1')
        if 'de9f2c7fd25e1b3afad3e85a0bd17d9b100db4b3' == SHA1(b"The quick brown fox jumps over the lazy cog"):
            print('Passed test 2')
            if 'da39a3ee5e6b4b0d3255bfef95601890afd80709' == SHA1(b''):
                print('Passed test 3')
            else:
                print('Failed test 3, please fix the implementation')
                raise Exception
        else:
            print('Failed test 2, please fix the implementation')
            raise Exception
    else:
        print('Failed test 1, please fix the implementation')
        raise Exception
    print('Your SHA1 implementation passed all tests!')
    print('\n')
    print('Comparing to hashlib SHA1 implementation')
    key = b'YELLOW SUBMARINE'
    message = b'HELLO THERE'
    if hashlib.sha1(key + message).hexdigest() == SHA1_MAC(key,message):
        print('Implementations match, good job!')
    else:
        print('Failed please cheak your implementation')
                
    