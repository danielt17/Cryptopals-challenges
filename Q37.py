# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 10:35:06 2021

@author: danie
"""


# https://cryptopals.com/sets/3/challenges/23

# %% Imports

from Q35 import MT19937MersenneTwisterRNG as MT19937
from z3 import BitVec,BitVecVal,Solver,LShR
from tqdm import tqdm
import numpy as np

# %% Functions

# two methods:
# "analytical" which isnt eleagnet.
# symbolic method using a modulator arithemtic sat solver (a very useful tool)
# 1. https://blog.ollien.com/posts/reverse-mersenne-twister/
# 2. https://www.schutzwerk.com/en/43/posts/attacking_a_random_number_generator/

# sat solving the recurrence relation
# LShR is the function: >>

def untemper(sequenceStream):
    y1 = BitVec('y1',32)
    y2 = BitVec('y2',32)
    y3 = BitVec('y3',32)
    y4 = BitVec('y4',32)
    y = BitVecVal(sequenceStream,32)
    s = Solver()
    equations = [
        y2 == y1 ^ (LShR(y1,11) & 0xFFFFFFFF), 
        y3 == y2 ^ ((y2 << 7) & 0x9D2C5680),
        y4 == y3 ^ ((y3 << 15) & 0xEFC60000),
        y == y4 ^ LShR(y4,18)
    ]
    s.add(equations)
    s.check()
    return s.model()[y1].as_long()

def recover_state_mt(numbers): 
    state = [] 
    for i in tqdm(range(len(numbers))): 
        state.append(untemper(numbers[i])) 
    return state

def generate_random_numbers(rng):
    randNumbers = []
    for i in range(rng.n+1):
        randNumbers.append(rng.extract_number())
    return randNumbers

def test_rng_equivalence(rngOriginal,rngEstimated,numExperiments = 1000):
    rngOriginalrand = []
    rngEstimatedrand = []
    rngEstimated.extract_number() # to fix syncronization error (yeah i can fix it by estimated the syncronization offset but it will constribute nothing to the problem)
    for i in range(numExperiments):
        rngOriginalrand.append(rngOriginal.extract_number()); 
        rngEstimatedrand.append(rngEstimated.extract_number()); 
    if rngOriginalrand ==rngEstimatedrand:
        return True
    else:
        return False
    
# %% Main

if __name__ == '__main__':
    seed = 532
    rngOriginal = MT19937(seed)
    print('\n')
    print("Generating random numbers")
    print('\n')
    randNumbers = generate_random_numbers(rngOriginal)
    statesOriginal = rngOriginal.MT
    print("Recovering mersenne twister states")
    print('\n')
    stateRecovered = recover_state_mt(randNumbers)[1:] # first estimate is wrong due to initialization as a result of seed
    print('\n')
    if stateRecovered == statesOriginal:
        print('State recovered succesfully')
    else:
        raise Exception('Failed to recover state')
    print('\n')
    rngEstimated = MT19937(1)
    rngEstimated.MT = stateRecovered
    if test_rng_equivalence(rngOriginal,rngEstimated):
        print('Success !!! Both generators produce the same random stream.')
    else:
        print('Failed :(')
    
    
        