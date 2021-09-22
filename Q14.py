# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 17:38:57 2021

@author: danie
"""

# %% Challange

# https://cryptopals.com/sets/1/challenges/4

# %% Imports 

from Q13 import BruteForceSingleByteXorCipher

# %% Functions
    
# %% Charcter frequency book

CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}

# %% Main

if __name__ == '__main__':
    lines = []
    with open('4.txt') as f:
        lines = f.readlines()
    bestScore = 0; bestKey = 0; bestDecypher = 0; bestLine = 0;
    for i in range(len(lines)):
        input_hex_string = lines[i]
        curScore,curKey,curDecypher = BruteForceSingleByteXorCipher(input_hex_string)
        if curScore > bestScore:
            bestScore = curScore
            bestKey = curKey
            bestDecypher = curDecypher
            bestLine = i 
    print('Decyphered text with key: ' + str(bestKey) + ' and score: ' + str(bestScore) + ' Cur line: ' + str(bestLine) + ' \n')
    print(str(bestDecypher))