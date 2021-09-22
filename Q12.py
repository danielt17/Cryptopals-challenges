# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 14:53:24 2021

@author: danie
"""

# %% Challange

# https://cryptopals.com/sets/1/challenges/2

# %% Functions

def strHex2bin(string):
    return bin(int(string,16))[2:]

def xorTwoBuffers(str1,str2):
    bitSeq1 = strHex2bin(str1)
    bitSeq2 = strHex2bin(str2)
    if len(bitSeq1) != len(bitSeq2):
        desiredLength = max(len(bitSeq1),len(bitSeq2))
        bitSeq1 = bitSeq1.zfill(desiredLength)
        bitSeq2 = bitSeq2.zfill(desiredLength)
    Xored = [int(_a) ^ int(_b) for _a, _b in zip(bitSeq1, bitSeq2)]
    resultXor = "".join([str(bits) for bits in Xored])
    resultXor = hex(int(resultXor,2))[2:]
    return resultXor

# %% Main

if __name__ == '__main__':
    str1 = '1c0111001f010100061a024b53535009181c'
    str2 = '686974207468652062756c6c277320657965'
    resultXor = xorTwoBuffers(str1,str2)
    solution = '746865206b696420646f6e277420706c6179'
    if solution == resultXor:
        print('Success')
    else:
        print('Try again')
    