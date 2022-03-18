# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 14:17:25 2021

@author: danie
"""

# https://cryptopals.com/sets/5/challenges/33

# %% Imports

from random import randint
from hashlib import sha256
from Crypto.Util.number import long_to_bytes

# %% Functions

# Implementations from wikipedia: https://en.wikipedia.org/wiki/Modular_exponentiation

# Memory-efficient method
def modexp_simple_method(base, exponent, modulus):
    if modulus == 1:
        return 0
    c = 1
    for ePrime in range(exponent):
        c = (c * base) % modulus
    return c

# Right-to-left binary method (exponentiation by squaring https://en.wikipedia.org/wiki/Exponentiation_by_squaring)
def modexp(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if (exponent % 2) == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

# Implementations from https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

class DiffieHellman:
    
    def __init__(self,p,g):
        self.p = p
        self.g = g
        self.a = randint(1,p)
        self.s = None
    
    def public_key(self):
        A = modexp(self.g,self.a,self.p)
        return A
    
    def shared_secret(self,B):
        self.s = modexp(B,self.a,self.p)
        return self.s
    
def run_diffie_hellman_exchange(p,g):
    print('\n')
    print('Running Diffie-Hellman key exchange: \n')
    print('g: ' + str(g) + '. p: '  + str(p))
    alice = DiffieHellman(p,g)
    bob = DiffieHellman(p,g)
    if alice.shared_secret(bob.public_key()) == bob.shared_secret(alice.public_key()):
        print('Alice shared secret: ' + str(alice.s) + '.')
        print('Bob shared secret: ' + str(bob.s) + '.')
        sharedSecret = alice.s
        return sharedSecret
    else:
        raise Exception('Diffie Hellman key exchanage failed')

# %% Main

if __name__ == '__main__':
    print('\n')
    if modexp_simple_method(4, 13, 497) == 445:
        print('Good implementation of modular exponentiation using the memory efficent method')
    else:
        print('Please fix your implementation of modular exponentiation using the memory efficent method')
    if modexp(4, 13, 497) == 445:
        print('Good implementation of modular exponentiation using the Right-to-left binary method')
    else:
        print('Please fix your implementation of modular exponentiation using the Right-to-left binary method')
    sharedSecret1 = run_diffie_hellman_exchange(p=37,g=5)
    print('Agreed secret key: ' + sha256(long_to_bytes(sharedSecret1)).hexdigest())
    p = int('ffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff',16)
    g = 2
    sharedSecret2 = run_diffie_hellman_exchange(p=p,g=g)
    print('Agreed secret key: ' + sha256(long_to_bytes(sharedSecret2)).hexdigest())
    
