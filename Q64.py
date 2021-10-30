# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 18:17:35 2021

@author: danie
"""


# https://cryptopals.com/sets/6/challenges/43

# %% Imports

from Q44 import SHA1
from Q51 import modexp
from Q57 import invmod
from Q63 import attack_on_dsa_fixed_nonce
# from pwn import *

# %% Functions
    
def load_data():
    with open('64.txt') as f:
        lines = f.readlines()
    data = []
    print('Recieved data: \n')
    for i in range(len(lines)//4):
        msg = lines[4*i    ][5:-1].encode()
        s = int(lines[4*i + 1][3:-1])
        r = int(lines[4*i + 2][3:-1])
        m = int(lines[4*i + 3][3:-1],16)
        data.append([msg,s,r,m])
        print('Msg: ' + str(msg) + ' s: ' + str(s) + ' r: ' + str(r) + ' m: ' + str(m) + '\n')
    return data

def estimate_private_key(m1,s1,m2,s2,q):
    estimated_k = (((m1 - m2) % q) * invmod((s1 - s2) % q,q)) % q
    return estimated_k

def brute_force_key(data,y,p,q,g):
    n_samples = len(data)
    for i in range(n_samples):
        for j in range(n_samples):
            try:
                estimated_k = estimate_private_key(data[i][3],data[i][1],data[j][3],data[j][1],q)
                estimated_private_key = attack_on_dsa_fixed_nonce(data[i][1],estimated_k,data[i][3],data[i][2],q)
                estimated_public_key = modexp(g,estimated_private_key,p)
                if estimated_public_key == y:
                    return estimated_private_key
            except:
                continue
    raise Exception('Didnt find private key, fix your brute force attack!')

# %% Main

if __name__ == '__main__':
    print('\n\n\n\n')
    print('DSA nonce recovery from repeated nonce \n')
    print('Known DSA parameters: \n')
    p = int('800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebeac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc871a584471bb1',16)
    q = int('f4f47f05794b256174bba6e9b396a7707e563c5b',16)
    g = int('5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119458fef538b8fa4046c8db53039db620c094c9fa077ef389b5322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a0470f5b64c36b625a097f1651fe775323556fe00b3608c887892878480e99041be601a62166ca6894bdd41a7054ec89f756ba9fc95302291',16)
    print('p: ' + str(p) + '\n')
    print('q: ' + str(q) + '\n')
    print('g: ' + str(g) + '\n')
    y = int('2d026f4bf30195ede3a088da85e398ef869611d0f68f0713d51c9c1a3a26c95105d915e2d8cdf26d056b86b8a7b85519b1c23cc3ecdc6062650462e3063bd179c2a6581519f674a61f1d89a1fff27171ebc1b93d4dc57bceb7ae2430f98a6a4d83d8279ee65d71c1203d2c96d65ebbf7cce9d32971c3de5084cce04a2e147821',16)
    print('Recieved public key: ' + str(y) + '\n')
    data = load_data()
    estimated_private_key = brute_force_key(data,y,p,q,g)
    print('Recovered private key: ' + str(estimated_private_key) + '\n')
    if  SHA1(hex(estimated_private_key)[2:].encode()) == 'ca8f6f7c66fa362d40760d135b763eb8527d3d52':
        print('Successfully got the flag! \n')
    else:
        print('Attack didnt fail, but there are problems with decoding the flag :( \n') 
    
