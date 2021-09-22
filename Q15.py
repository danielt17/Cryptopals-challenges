# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 18:05:50 2021

@author: danie
"""

# %% Challange

# https://cryptopals.com/sets/1/challenges/5

# %% Imports

from binascii import hexlify

# %% Functions

def repeatingKeyXOR(input_bytes, key_value):
    output = b''
    i = 0; keyLength = len(key_value)
    for char in input_bytes:
        output += bytes([char ^ key_value[i]])
        i = (i + 1)%keyLength
    return output

# %% Main

if __name__ == '__main__':
    inputBytes = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = b"ICE"
    output = repeatingKeyXOR(inputBytes, key)
    if str(hexlify(output), "utf-8") ==  "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f":
        print('sucess')
    else:
        print('fail')