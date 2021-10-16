# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 12:41:08 2021

@author: danie
"""


# https://cryptopals.com/sets/6/challenges/41

# %% Imports

from Q51 import modexp
from Q57 import generate_prime_number,invmod,str_to_num_for_rsa,num_to_str_for_rsa
from hashlib import sha256
from time import time
from random import randrange
import sys
sys.setrecursionlimit(1500)

# %% Functions

class RSAUnpaddedMessageRecoveryOracle:
    
    def __init__(self):
        self.succed_in_suitable_primes = False # we need phi_n to be coprime to e therefore looping until we find suitable primes for this condition
        while not self.succed_in_suitable_primes:
            try:
                self.p = generate_prime_number()
                self.q = generate_prime_number()
                self.n = self.p * self.q
                self.phi_n = (self.p-1) * (self.q-1) # if p is prime the number of euler totient function is p -1 as all the numbers below p are coprime to p,  the multiplcation is done because the totient function is multiplicative
                self.e = 3
                self.d = invmod(self.e,self.phi_n)
                self.succed_in_suitable_primes = True
            except:
                continue
        self.public_key = [self.e,self.n]
        self.private_key = [self.d,self.n]
        self.log = [[],[]] # 1. time 2. ciphertext hashes
        
    def send_public_key(self):
        return self.public_key
        
    def encrypt(self,plainText,public_key=None):
        if public_key is None:
            public_key = self.public_key
        return modexp(str_to_num_for_rsa(plainText), public_key[0], public_key[1])

    def decrypt(self,cipherText):
        hashed = sha256(str(cipherText).encode()).hexdigest()
        if hashed in self.log[1]:
            raise Exception('Cipher text already submmited for decryption')
        self.log[0].append(time()); 
        self.log[1].append(hashed); 
        return modexp(cipherText, self.private_key[0], self.private_key[1])

def attack(plainText,Oracle):
    print('Attacking unpadded rsa: \n')
    pub_key = Oracle.send_public_key()
    print('Public key recieved: ' + str(pub_key) + '\n')
    cipherText = Oracle.encrypt(plainText)
    print('Cipher text recieved: ' + str(cipherText) + '\n')
    Oracle.decrypt(cipherText)
    print('cipher text is logged in the log: ' + str(Oracle.log) + '\n')
    try:
        Oracle.decrypt(cipherText)
    except:
        print('Cant decrypt the message as it is already in log \n')
    S = randrange(1,pub_key[1])
    print('Randomly generated S: ' + str(S) + '\n')
    C_ = (modexp(S,pub_key[0],pub_key[1]) * cipherText) % pub_key[1]
    print("Sending C': " + str(C_) + " to be decrypted \n")
    P_ = Oracle.decrypt(C_)
    print("Decrypted C' which is P': " + str(P_) + '\n')
    print("Calcualting plain text by inverting the P' using the random S \n")
    recoveredPlainText = P_ * invmod(S,pub_key[1]) % pub_key[1]
    print('Recovered plain text: ' + str(num_to_str_for_rsa(recoveredPlainText)) + '\n')
    
# %% Main

if __name__ == '__main__':
    plainText = 'Hello there!'
    print('\n \n \n \n')
    print('Plain text: ' + plainText + '\n')
    Oracle = RSAUnpaddedMessageRecoveryOracle()
    attack(plainText,Oracle)
    
    