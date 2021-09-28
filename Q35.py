# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 17:53:59 2021

@author: danie
"""

# https://cryptopals.com/sets/3/challenges/21

# %% Imports

import numpy as np

# %% Functions

def get_lowest_w_bits(n, nBits):
    zeroingMask = (1 << nBits) - 1
    return n & zeroingMask

# implementation of the paper: "Mersenne Twister: A 623-dimensionally equidistributed unifrom pseudorandom number genertor"
class MT19937MersenneTwisterRNG:
       
    # Setting up MT19937 parameters from wikipedia (32-bit version)
    def __init__(self,seed):
        self.w = 32; self.n = 624; self.m = 397; self.r = 31;
        self.a = 0x9908B0DF
        self.u = 11; self.d = 0xFFFFFFFF
        self.s = 7; self.b = 0x9D2C5680
        self.t = 15; self.c = 0xEFC60000
        self.L = 18
        self.f = 1812433253 
        self.MT = [0]*self.n
        self.index = self.n
        self.lower_mask = (1 << self.r) - 1
        self.upper_mask = get_lowest_w_bits(not self.lower_mask, self.w)
        self.seed = seed
        self.seed_mt()
    
    # Initialize the generator from a seed
    def seed_mt(self):
        self.index = self.n-1
        self.MT[0] = self.seed
        for i in range(1,self.n):
            self.MT[i] = get_lowest_w_bits(self.f * (self.MT[i-1] ^ (self.MT[i-1] >> (self.w - 2))) + i, self.w)
    
    # Extracting tempered value based on MT[index]
    def extract_number(self):
        if self.index >= self.n:
            if self.index > self.n:
                raise Exception('Generator was never seeded')
            self.twist()
        y = self.MT[self.index]
        y = y ^ ((y >> self.u) & self.d)
        y = y ^ ((y << self.s) & self.b)
        y = y ^ ((y << self.t) & self.c)
        y = y ^ (y >> 1)
        self.index = self.index + 1
        return get_lowest_w_bits(y,self.w)
    
    # Generate the next n values from the series x_i 
    def twist(self):
        for i in range(self.n):
            x = (self.MT[i] & self.upper_mask) + (self.MT[(i+1) % self.n] & self.lower_mask)
            xA = x >> 1
            if ((x % 2) != 0):
                xA = xA ^ self.a
            self.MT[i] = self.MT[(i+self.m) % self.n] ^ xA
        self.index = 0

# %% Main

if __name__ == '__main__':
    setOfAllGeneratedNumberes = []
    print('\n')
    print('Testing random number generator (MT19937 Mersenne Twister): ')
    nSeeds = 10; nReapets = 5
    for seed in range(nSeeds):
        rng = MT19937MersenneTwisterRNG(seed)
        for i in range(nReapets):
            setOfAllGeneratedNumberes.append(rng.extract_number())
    setOfAllGeneratedNumberes = np.array(setOfAllGeneratedNumberes)
    occurences = np.unique(setOfAllGeneratedNumberes)
    print('\n')
    if len(occurences) == nSeeds*nReapets:
        print('Seems like the random number generator is implemented correctly')
    print('\n')
    