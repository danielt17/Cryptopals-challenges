# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 22:41:12 2021

@author: danie
"""

# %% Challange

# https://cryptopals.com/sets/1/challenges/6

# %% Imports

import numpy as np
from Q13 import getAllcharctersEncodingInascii,SingleByteXorCipher,get_english_score
from Q15 import repeatingKeyXOR
from tqdm import tqdm
from base64 import b64decode

# %% Functions

def HammingDistanceBytes(bytes1,bytes2):
    distanceTemp = "{0:b}".format(bytes1 ^ bytes2)
    distance = 0
    for ind in distanceTemp:
        distance = int(ind) + distance
    return distance

def HammingDistanceStrings(str1,str2):
    HammingLen = 0
    for i in range(len(str1)):
        HammingLen = HammingLen + HammingDistanceBytes(str1[i],str2[i])
    return HammingLen

def LoadCypherText():
    with open('16.txt') as f:
        cypherText = b64decode(f.read())
    return cypherText

def ScoreKeySize(KEYSIZE,cypherText):
    bytesKEYSIZE1 = cypherText[:KEYSIZE]; bytesKEYSIZE2 = cypherText[KEYSIZE:2*KEYSIZE]
    bytesKEYSIZE3 = cypherText[2*KEYSIZE:3*KEYSIZE]; bytesKEYSIZE4 = cypherText[3*KEYSIZE:4*KEYSIZE]
    bytesKEYSIZE5 = cypherText[4*KEYSIZE:5*KEYSIZE]; bytesKEYSIZE6 = cypherText[5*KEYSIZE:6*KEYSIZE]
    scoreKeySize = np.average([HammingDistanceStrings(bytesKEYSIZE1,bytesKEYSIZE2)/KEYSIZE, HammingDistanceStrings(bytesKEYSIZE3,bytesKEYSIZE4)/KEYSIZE,HammingDistanceStrings(bytesKEYSIZE5,bytesKEYSIZE6)/KEYSIZE])
    return scoreKeySize

def BruteForceSingleByteXorCipher(bitSeq1):
    
    CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
    }
    
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


def BreakCypher(KEYSIZEestimated,cypherText):
    decypheredtext = []
    keys = []
    for KEYSIZEcurrent in tqdm(KEYSIZEestimated):
        key = b''
        for i in range(KEYSIZEcurrent):
            block = b''
            for j in range(i, len(cypherText), KEYSIZEcurrent):
                block += bytes([cypherText[j]])
            key += bytes([BruteForceSingleByteXorCipher(block)[1]])
        keys.append(key)
        decypheredtext.append(repeatingKeyXOR(cypherText,key))
    englishScores = []; 
    for decypher in decypheredtext:
        englishScores.append(get_english_score(decypher))
    best = np.argmax(englishScores)
    return keys[best],decypheredtext[best],KEYSIZEestimated[best]
        
# %% Main

if __name__ == '__main__':
    # 1
    KEYSIZES = np.int64(np.linspace(2,40,39))
    # 2
    EnbTest = False
    if EnbTest:
        str1 = b'this is a test' 
        str2 = b'wokka wokka!!!'
        HammingDistance = HammingDistanceStrings(str1,str2)
        if HammingDistance == 37:
            print('Hamming distance with respect to bits passed succesfully\n')
        else:
            print('Please fix your hamming distance algorithm')
    # 3 + 4
    cypherText = LoadCypherText()
    KEYSIZEscores = []
    for KEYSIZE in KEYSIZES:
        KEYSIZEscores.append(ScoreKeySize(KEYSIZE,cypherText))
    KEYSIZEestimated = KEYSIZES[np.argsort(KEYSIZEscores)][:5]
    # 5 + 6 + 7 + 8 
    key,decypheredtext,KEYSIZEestimated = BreakCypher(KEYSIZEestimated,cypherText)
    print('\n')
    print('Key: ' + str(key) + ' \n')
    print('Key size: ' + str(KEYSIZEestimated) + ' \n')
    print('Plain text: ' + str(decypheredtext) + ' \n')
    
    
        

    
