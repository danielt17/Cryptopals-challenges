# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 14:41:13 2023

@author: danie
"""


# %% Imports

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from itertools import product

# %% Define Merkle Damagard hash function

class MD():
    
    def __init__(self, H, H_len):
        self.H_len = H_len
        self.H = H
    
    def pad_to_block_size(self,m):
        if len(m) % AES.block_size != 0:
            m_padded = pad(m,AES.block_size)
        else:
            m_padded = m
        return m_padded
    
    def digest(self,m):
        m_padded = self.pad_to_block_size(m)
        for i in range(0,len(m_padded),AES.block_size):
            self.H = self.pad_to_block_size(self.H)
            m_block = m_padded[i:i+AES.block_size]
            self.H = AES.new(self.H,AES.MODE_ECB).encrypt(m_block)
            self.H = self.H[:self.H_len]
        return self.H

# %% Find Collisions

def find_collision(m1, H, H_len):
    m1_digest = MD(H, H_len).digest(m1)
    while True:
        m2 = get_random_bytes(AES.block_size)
        if m1 != m2:
            m2_digest = MD(H, H_len).digest(m2)
            if m1_digest == m2_digest:
                H_new = m2_digest
                return m1, m2, H_new
        else:
            continue

def generate_collisions(num_collisions, H, H_len):
    ms = []
    for _ in range(num_collisions):
        m1 = get_random_bytes(AES.block_size)
        m1, m2, H = find_collision(m1, H, H_len)
        ms.append((m1,m2))
    
    # Cartezian multiplication of all possible continuations
    for i in product([0, 1], repeat=num_collisions):
        yield b''.join([m[i[idx]] for idx, m in enumerate(ms)])

# %% Cascadaded Hash function digest:
    
def h(m, f_H, g_H, bf, bg):
    f = MD(f_H, bf).digest(m)
    g = MD(g_H, bg).digest(m)
    return f+g

# %% Part 1 - Finding multicollisions in a single hash function in sublinear time

def Part1():
    num_collisions = 4
    H_len = 2
    H = get_random_bytes(H_len)
    ms_generator = generate_collisions(num_collisions, H, H_len)
    ms = [m for m in ms_generator]
    hashs = [MD(H, H_len).digest(m) for m in ms]
    if hashs.count(hashs[0]) == 2**4:
        print(f"Succsefully found: {2**num_collisions} collisions")
    else:
        raise Exception("Havn't found all possible collisions")

# %% Part 2 - Finding multicollisions in a cascaded hash function in sublinear time

def Part2():
    bf = 2
    bg = 4
    f_H = get_random_bytes(bf)
    g_H = get_random_bytes(bg)
    num_collisions_of_f_to_find = bg*4
    found_collision = False
    while not found_collision:
        f_ms = generate_collisions(num_collisions_of_f_to_find, f_H, bf)
        hashes_dict = {}
        for f_m in f_ms:
            digested = MD(g_H, bg).digest(f_m)
            if digested in hashes_dict:
                f_g = hashes_dict[digested]
                m1, m2 = f_m, f_g
                found_collision = True
                break;
            else:
                hashes_dict[digested] = f_m
    if h(m1, f_H, g_H, bf, bg) == h(m2, f_H, g_H, bf, bg):
        print(f"Succsefully found a collision")
    else:
        raise("Didn't find a collision")
        
# %% Main

def main():
    Part1()
    Part2()

# %% Run main

if __name__ == "__main__":
    main()