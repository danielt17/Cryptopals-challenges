# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 14:30:42 2022

@author: danie
"""


# https://cryptopals.com/sets/6/challenges/47

# %% Imports

from Q51 import modexp
from Q57 import generate_prime_number,invmod
from Crypto.Util.number import long_to_bytes
import sys
from random import getrandbits
from math import ceil,floor

sys.setrecursionlimit(1500)

# %% Functions

class RSAPCKS1PaddingOracle:
    
    def __init__(self,prime_size=128):
        print('Generating valid RSA parameters:\n')
        self.succed_in_suitable_primes = False # we need phi_n to be coprime to e therefore looping until we find suitable primes for this condition
        while not self.succed_in_suitable_primes:
            try:
                self.p = generate_prime_number(prime_size)
                self.q = generate_prime_number(prime_size)
                self.n = self.p * self.q
                self.phi_n = (self.p-1) * (self.q-1) # if p is prime the number of euler totient function is p -1 as all the numbers below p are coprime to p,  the multiplcation is done because the totient function is multiplicative
                self.e = 3
                self.d = invmod(self.e,self.phi_n)
                self.succed_in_suitable_primes = True
            except:
                continue
        self.k = len(long_to_bytes(self.n)) # length of modulos (in terms of bytes)
        self.public_key = [self.e,self.n]
        self.private_key = [self.d,self.n]
        print('Generated RSA paramters: \n')
        print('Public key: ' + str(self.public_key) + '\n')
        print('Private key: ' + str(self.private_key) + '\n')
        
    def send_public_key(self):
        return self.public_key
        
    def PKCS1_pad(self,plainTextBytes):
        # Implemented according to RFC 3447 
        # https://datatracker.ietf.org/doc/html/rfc3447#page-23
        PS = b''
        for _ in range(self.k - len(plainTextBytes) - 3): 
            PS_current = 0
            while PS_current == 0:
                PS_current = getrandbits(8)
            PS = PS +  long_to_bytes(PS_current)
        return b'\x00\x02' + PS + b'\x00' + plainTextBytes
    
    def encrypt(self,plainText):
        # plainText input as bytes object
        plainTextPadded = int.from_bytes(self.PKCS1_pad(plainText),'big')
        return modexp(plainTextPadded, self.public_key[0], self.public_key[1])

    def decrypt(self,cipherText):
        return modexp(cipherText, self.private_key[0], self.private_key[1])
    
    def check_valid_padding(self,decrypted_text):
        return True & (decrypted_text[0] == 0) & (decrypted_text[1] == 2)
    
    def padding_oracle(self,cipherText):
        decrypted_text = long_to_bytes(self.decrypt(cipherText),self.k)
        validation_value = self.check_valid_padding(decrypted_text);
        return validation_value
    
    def decrypt_and_unpad(self,cipherText):
        decrypted_text = long_to_bytes(self.decrypt(cipherText),self.k)
        validation_value = self.check_valid_padding(decrypted_text);
        if validation_value:
            i = 2
            while decrypted_text[i] != 0:
                i = i + 1
            return decrypted_text[(i + 1):]
        else:
            raise Exception('Decryption failed!')
        
def Bleichenbacher_98_attack(RSA,cipherText,public_key):
    # Implementation of Bleichenbacher's 98 attack
    # Taken from the paper: Chosen Ciphertext Attacks Against Protocols Based on the RSA Encryption Standard PKCS #1
    # Link: http://archiv.infsec.ethz.ch/education/fs08/secsem/bleichenbacher98.pdf
    print("Starting Bleichenbacher's PKCS 1.5 attack: \n")
    c = cipherText; e = public_key[0]; n = public_key[1];
    B = 2**(8*(RSA.k-2))
    # Step 1: Blinding. (we don't actually need it cause c is known to be PKCS conforming)
    print('Step 1: Blinding.\n')
    print('Intializing c (the cipher text is already PKCS conforming): ' + str(c) + '\n')
    M = [2*B, 3*B - 1] # This is the range between \x00\x02\x00...\x00  to \x00\x02\xff...\xff
    print('Intializing M limits [2*B, 3*B-1]: ' + str(M) + '\n')
    i = 1;
    print('Intializing i: ' + str(i) + '\n')
    # Step 2: Searching for PKCS conforming messages
    print('Step 2: Searching for PKCS conforming messages.\n')
    print('Step 2.a: Starting the search.\n')
    s_cur = ceil(n/(3*B))
    while not RSA.padding_oracle((c * modexp(s_cur, e, n)) % n):
        s_cur = s_cur + 1
    print('Step 2.b: Searching with more than one interval left. --- CURRENTLY NOT IMPLEMENTED! --- \n')
    print('Step 2.c: Searching with one interval left.\n')
    r_cur = ceil(2 * (M[1] * s_cur - 2 * B)/n)
    s_next = ceil((2 * B + r_cur * n)/M[1])
    while not RSA.padding_oracle((c * modexp(s_next, e, n)) % n):
        if s_next == floor((3 * B + r_cur * n)/M[0]):
            r_cur = r_cur + 1
            s_next = ceil((2 * B + r_cur * n)/M[1])
        else:
            s_next = s_next + 1
    # Step 3: arrowing the set of solutions
    print('Step 3: Narrowing the set of solutions.\n')
    r_lower = ceil((M[0] * s_next - 3 * B + 1)/n)
    r_upper = floor((M[1]*s_next - 2 * B)/n)
    Ms = []
    for rs in range(r_lower,r_upper + 1):
        upper = max(M[0],ceil((2 * B + rs * n)/s_next))
        lower = min(M[1],floor((3 * B - 1  + rs * n)/s_next))
        Ms.append([upper,lower])
    # Step 4: Computing the solution
    print('Step 4: Computing the solution.\n')
    if len(Ms) == 1:
        amount = Ms[0][1] - Ms[0][0]
        if amount <= 100:
            m = []
            for value in range(Ms[0][0],Ms[0][1]):
                m.append(long_to_bytes(value % n,RSA.k))
            return m
        else:
            raise Exception('To many values inside single union: ' + str(amount))
    else:
        raise Exception('To many values in union (' +  str(len(Ms)) + '), we solve this case in Q68')
    
        
# %% Main

if __name__ == '__main__':
    print('\n\n\n')
    print("Bleichenbacher's PKCS 1.5 padding oracle attack (Simple case): \n")
    print('\n\n\n')
    prime_size = 128
    plainText = b"kick it, CC"
    RSA = RSAPCKS1PaddingOracle(prime_size)
    print('Plain text to be encrypted: ' + str(plainText) + '\n')
    cipherText = RSA.encrypt(plainText)
    print('Cipher text to be sent over unsecure line: ' + str(cipherText) + '\n')
    print('Interecpting cipher text using man in the middle, received data:\n')
    public_key = RSA.send_public_key()
    print('Received public key: ' + str(public_key))
    print('Received cipher text: ' + str(cipherText) + '\n')
    print('\n\n\n')
    recovered_plainText = Bleichenbacher_98_attack(RSA,cipherText,public_key)
    print('Important this version of the attack works sometimes for small prime sizes (16), to see the full version go to Q68.\n')
    print('\n\n\n')
    





