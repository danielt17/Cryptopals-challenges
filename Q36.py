# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 19:02:23 2021

@author: danie
"""

# https://cryptopals.com/sets/3/challenges/22

# %% Imports

from Q35 import MT19937MersenneTwisterRNG
import numpy as np
from time import time

# %% Functions

def generate_in_random_time_number_with_respect_to_seed():
    global timeStampSeed
    timeStampSeed = timeStampSeed + np.random.randint(40,1000)
    seed = timeStampSeed
    rng = MT19937MersenneTwisterRNG(seed).extract_number()
    timeStampSeed = timeStampSeed + np.random.randint(40,1000)
    return seed,rng
    
def crack_mt19937_seed(rngTruth):
    crackedSeed = timeStampSeed + np.random.randint(40,1000)
    while MT19937MersenneTwisterRNG(crackedSeed).extract_number() != rngTruth:
        crackedSeed = crackedSeed - 1
    return crackedSeed

# %% Main

if __name__ == '__main__':
    timeStampSeed = int(time())
    seed,rngTruth = generate_in_random_time_number_with_respect_to_seed()
    crackedSeed = crack_mt19937_seed(rngTruth)
    if crackedSeed == seed:
        print('Cracked the seed !')
    else:
        print('Cracking failed !')
    
