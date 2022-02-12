# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 14:05:49 2022

@author: danie
"""


# https://cryptopals.com/sets/6/challenges/45

# %% Imports

from Q44 import SHA1
from Q51 import modexp
from Q57 import invmod
from random import randint

# %% Functions

# implemenated using the description from wikipedia:
# https://en.wikipedia.org/wiki/Digital_Signature_Algorithm
class DSA:
    
    def __init__(self,p,q,g):
        print('Offer p, q and g parameters: \n')
        self.p = p
        self.q = q
        self.g = g
        print('p: ' + str(self.p) + '\n')
        print('q: ' + str(self.q) + '\n')
        print('g: ' + str(self.g) + '\n')
        
    def generate_keys(self):
        print('Generating DSA keys: \n')
        private_key = randint(1,self.q-1)
        public_key = modexp(self.g,private_key,self.p)
        print('Generated private key: ' + str(private_key) + '\n')
        print('Generated public key: ' + str(public_key) + '\n')
        return private_key,public_key
    
    def sign_message(self,message,private_key):
        # message is an input as a bytes object
        message_hash = int(SHA1(message),16)
        k = randint(1,self.q-1)
        r = modexp(self.g,k,self.p) % self.q
        s = (invmod(k,self.q) * (message_hash + private_key * r)) % self.q
        print('Generated message verifiers: \n')
        print('r: ' + str(r) + '\n')
        print('s: ' + str(s) + '\n')
        return r,s
    
    def verify_message(self,message,r,s,public_key):
        print('Recieved: \n')
        print('Message: ' + str(message) + '\n')
        print('r: ' + str(r) + '\n')
        print('s: ' + str(s) + '\n')
        print('public_key: ' + str(public_key) + '\n')
        print('Verifing the message: \n')
        message_hash = int(SHA1(message),16)
        w = invmod(s,self.q)
        u1 = (message_hash * w) % self.q
        u2 = (r * w) % self.q
        v = ((modexp(self.g,u1,self.p)*modexp(public_key,u2,self.p)) % self.p) % self.q
        if v == r:
            print('Message verified \n')
        else:
            print('Message isnt verified \n')

# %% Main

if __name__ == '__main__':
    print('\n\n\n\n')
    print('DSA parameter tampering, man in the middle (MITM) attack\n')
    p = int('800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebeac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc871a584471bb1',16)
    q = int('f4f47f05794b256174bba6e9b396a7707e563c5b',16)
    g = int('5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119458fef538b8fa4046c8db53039db620c094c9fa077ef389b5322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a0470f5b64c36b625a097f1651fe775323556fe00b3608c887892878480e99041be601a62166ca6894bdd41a7054ec89f756ba9fc95302291',16)
    print('We offer the server bad generator parameters, where g = 0\n')
    g_tempter_0 = 0
    dsa = DSA(p,q,g_tempter_0)
    message = b'Hello, world'
    print('We want to sign the message: ' + str(message) + '\n')
    private_key,public_key = dsa.generate_keys()
    r,s = dsa.sign_message(message,private_key)
    print('We see our r parameter which we use to verify i: 0, we can now sign any message, and forge a signature: \n')
    forged_message = b'Goodbye, world'
    print('We use the given r,s and public key parameters to sign a different message: ' + str(forged_message))
    dsa.verify_message(forged_message,r,s,public_key)
    print('Forged message is verifyed and we bypass the authentication scheme!\n')
    print('\n\n\n')
    print('We offer the server a second type of bad generator parameters, where g = p + 1\n')
    g_temper_p_plus_1 = p + 1
    dsa1 = DSA(p,q,g_temper_p_plus_1)
    print('We want to sign the message: ' + str(message) + '\n')
    private_key,public_key = dsa1.generate_keys()
    print('We get a bad public key with value: 1, because (p+1)^p_key mod p = 1\n')
    r,s = dsa1.sign_message(message,private_key)
    print('We see that in the same way, we force r = 1\n')
    print('We use the given r,s and public key parameters to sign a different message: ' + str(forged_message))
    dsa1.verify_message(forged_message,r,s,public_key)
    print('Forged message is verifyed and we bypass the authentication scheme!\n')
    print('Successful demonstration off Man in the middle attack on DSA using parameter tampering')
    
    
    
        
