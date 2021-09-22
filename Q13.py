# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 16:11:58 2021

@author: danie
"""


# %% Challange

# https://cryptopals.com/sets/1/challenges/3

# %% Functions

def SingleByteXorCipher(input_bytes, key_value):
    output = b''
    for char in input_bytes:
        output += bytes([char ^ key_value])
    return output

def getAllcharctersEncodingInascii():
    asciiTable = []
    for i in range(256):
        asciiTable.append(i)
    return asciiTable

def hex2Ascii(hex_string):
    ascii_string = bytes.fromhex(hex_string).decode("ASCII")
    return ascii_string

def get_english_score(input_bytes):
    score = 0
    for byte in input_bytes:
        score += CHARACTER_FREQ.get(chr(byte).lower(), 0)
    return score

def BruteForceSingleByteXorCipher(input_hex_string):
    bitSeq1 = bytes.fromhex(input_hex_string)
    allCharcters = getAllcharctersEncodingInascii()
    bestScore = 0; bestKey = 0; bestDecypher = 0;
    for charCur in allCharcters:
        bitSeq2 = charCur
        output = SingleByteXorCipher(bitSeq1,bitSeq2)
        curScore = get_english_score(output)
        if curScore > bestScore:
            bestScore = curScore;
            bestKey = bitSeq2;
            bestDecypher = output;
    return bestScore,bestKey,bestDecypher
    
# %% Charcter frequency book

CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}

# %% Main

if __name__ == '__main__':
    bitSeq1 = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    allCharcters = getAllcharctersEncodingInascii()
    bestScore = 0; bestKey = 0; bestDecypher = 0;
    for charCur in allCharcters:
        bitSeq2 = charCur
        output = SingleByteXorCipher(bitSeq1,bitSeq2)
        curScore = get_english_score(output)
        if curScore > bestScore:
            bestScore = curScore;
            bestKey = bitSeq2;
            bestDecypher = output;
        print('Current char: ' + str(bitSeq2) + ' Score: ' + str(curScore) + ' current deciphered result: ' + str(output) + ' \n')
    print('Decyphered text with key: ' + str(bestKey) + ' and score: ' + str(bestScore) + ' \n')
    print(str(bestDecypher))
    
