# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 23:57:55 2021

@author: danie
"""


# https://cryptopals.com/sets/4/challenges/32

# %% Imports

from Q47attacker import time_leak_side_channel_attack

# %% Main

if __name__ == '__main__':
    fileName = 'GetZeroDayed'
    numExperiments = 5
    estimatedHMACSigniture = time_leak_side_channel_attack(fileName,numExperiments)
    print('File name: ' + fileName + ' . Estimated HMAC: ' + str(estimatedHMACSigniture))