# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 15:41:58 2022

@author: danie
"""


# https://cryptopals.com/sets/6/challenges/41

# %% Imports

from Q51 import modexp
from Q57 import generate_prime_number,invmod
from Crypto.Util.number import long_to_bytes
import sys
from base64 import b64decode
from tqdm import tqdm
from decimal import Decimal, getcontext
from time import sleep

sys.setrecursionlimit(1500)

# %% Functions

class RSAParityOracle:
    
    def __init__(self):
        print('Generating valid RSA parameters:\n')
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
        print('Generated RSA paramters: \n')
        print('Public key: ' + str(self.public_key) + '\n')
        print('Private key: ' + str(self.private_key) + '\n')
        
    def send_public_key(self):
        return self.public_key
        
    def encrypt(self,plainText):
        return modexp(plainText, self.public_key[0], self.public_key[1])

    def decrypt(self,cipherText):
        return modexp(cipherText, self.private_key[0], self.private_key[1])
    
    def decrypt_parity_oracle(self,cipherText):
        recovered_Text = self.decrypt(cipherText)
        # Return true for even number, false for odd number
        if recovered_Text % 2 == 0:
            return True
        else:
            return False

def RSAParityOracleAttack(cipherText,public_key,RSA):
    print('\n\n')
    print('Running RSA Parity oracle attack\n')
    print('The attacks works by abusing the fact when we wrap the modulos we expect the value of the decryption to be odd, because n is odd. Therefore, simple binary search can recover the plain text with resepct to wrapping to modulos.\n')
    print('\n\n')
    sleep(10)
    iter_num = len(long_to_bytes(public_key[1]))*8
    low = Decimal(0); high = Decimal(public_key[1]) # normal division and not // so i will get the last letter
    getcontext().prec = iter_num
    cipherText_of_2 = modexp(2, public_key[0], public_key[1]) # we need to use the cipherText analog of 2
    pbar = tqdm(total=iter_num)
    for i in range(iter_num):
        cipherText = (cipherText * cipherText_of_2) % public_key[1]
        if RSA.decrypt_parity_oracle(cipherText):
            high = (low + high)/2
        else:
            low = (low + high)/2
        print('Current decryption: ' + str(long_to_bytes(high)) + '\n')
        if (i+1) % 16 == 0:
            pbar.update(16)
    pbar.close()
    return high

# %% Main

if __name__ == '__main__':
    print('\n\n\n\n\n')
    print('Demonstration of RSA parity oracle attack\n')
    print('\n')
    plainText = b64decode('VGhhdCdzIHdoeSBJIGZvdW5kIHlvdSBkb24ndCBwbGF5IGFyb3VuZCB3aXRoIHRoZSBGdW5reSBDb2xkIE1lZGluYQ==')
    print('Plain text: ' + str(plainText) + '\n')
    plainText_int = int.from_bytes(plainText,'big')
    RSA = RSAParityOracle()
    cipherText = RSA.encrypt(plainText_int)
    public_key = RSA.send_public_key()
    print('Received public key: e = ' + str(public_key[0]) + ' , n = ' + str(public_key[1]) +  '\n')
    print('Received cipher text: ' + str(cipherText) + '\n')
    high = RSAParityOracleAttack(cipherText,public_key,RSA)
    plainText_recover = long_to_bytes(high)
    print('\n\n\n')
    print('Recovered plain text: ' + str(plainText_recover) + '\n')
    print('\n\n')
    if plainText_recover == plainText:
        print('Successfully recovered plain text!')
    else:
        print('Failed to recover plain text!')
    print('\n\n')
    
    
