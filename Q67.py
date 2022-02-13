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
from time import sleep

sys.setrecursionlimit(1500)

# %% Functions

class RSAPCKS1PaddingOracle:
    
    def __init__(self,prime_size=128):
        print('Generating valid RSA-' + str(prime_size*2) + ' parameters:\n')
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
            
    def remove_pkcs(self,text):
        i = 2
        while text[i] != 0:
            i = i + 1
        return text[(i + 1):]
        
def ceil(a, b):
    return (a + b - 1) // b

def append_and_merge(intervals, lower_bound, upper_bound):
    for i, (a, b) in enumerate(intervals):
        if not (b < lower_bound or a > upper_bound):
            new_a = min(lower_bound, a)
            new_b = max(upper_bound, b)
            intervals[i] = new_a, new_b
            return
    intervals.append((lower_bound, upper_bound))

def Bleichenbacher_98_attack(cipherText, RSA):
    # Implementation of Bleichenbacher's 98 attack
    # Taken from the paper: Chosen Ciphertext Attacks Against Protocols Based on the RSA Encryption Standard PKCS #1
    # Link: http://archiv.infsec.ethz.ch/education/fs08/secsem/bleichenbacher98.pdf
    print("Starting Bleichenbacher's PKCS 1.5 attack: \n")
    e = RSA.e; n = RSA.n;
    B = 2 ** (8 * (RSA.k - 2))
    # Step 1: Blinding. (we don't actually need it cause c is known to be PKCS conforming)
    c = cipherText
    print('Step 1: Blinding.\n')
    print('Intializing c (the cipher text is already PKCS conforming): ' + str(c) + '\n')
    M = [(2 * B, 3 * B - 1)] # This is the range between \x00\x02\x00...\x00  to \x00\x02\xff...\xff
    print('Intializing M limits [2*B, 3*B-1]: ' + str(M) + '\n')
    i = 1;
    Calls_to_oracle = 0;
    print('Intializing i: ' + str(i) + '\n')
    print("Starting Bleichenbacher's attack iterative loop:\n")
    while True:
        print('Iteration number: ' + str(i) + '\n')
        print('--------------------------------------\n')
        # Step 2: Searching for PKCS conforming messages
        print('Step 2: Searching for PKCS conforming messages.\n')
        if i == 1:
            print('Step 2.a: Starting the search.\n')
            s = ceil(n,3*B)
            while not RSA.padding_oracle((c * modexp(s, e, n)) % n):
                s = s + 1
                Calls_to_oracle += 1
                if Calls_to_oracle % 10000 == 0:
                    print('Calls to Oracle: ' + str(Calls_to_oracle))
        elif len(M) >= 2:
            print('Step 2.b: Searching with more than one interval left.\n')
            s = s + 1
            while not RSA.padding_oracle((c * modexp(s, e, n)) % n):
                s = s + 1
                Calls_to_oracle += 1
                if Calls_to_oracle % 10000 == 0:
                    print('Calls to Oracle: ' + str(Calls_to_oracle))
        elif i > 1 and len(M) == 1:
            print('Step 2.c: Searching with one interval left.\n')
            a = M[0][0]; b = M[0][1];
            if a == b: break
            r = ceil(2*(b * s - 2 * B),n)
            s = ceil(2 * B + r * n,b)
            while not RSA.padding_oracle((c * modexp(s, e, n)) % n):
                s = s + 1
                if s > (3 * B + r * n)//a:
                    r = r + 1
                    s = ceil(2 * B + r * n,b) 
                Calls_to_oracle += 1
                if Calls_to_oracle % 10000 == 0:
                    print('Calls to Oracle: ' + str(Calls_to_oracle))
        # Step 3: arrowing the set of solutions
        print('Step 3: Narrowing the set of solutions.\n')
        Ms = []
        for j in range(len(M)):
            a = M[j][0]; b = M[j][1]
            r_lower = ceil(a * s - (3 * B) + 1,n)
            r_upper = (b * s - (2 * B))//n
            for r in range(r_lower,r_upper + 1):
                lower = max(a,ceil(2 * B + r * n,s))
                upper = min(b,(3 * B - 1  + r * n)//s)
                # if lower > upper:
                    # raise Exception('Lower is bigger than upper!')
                append_and_merge(Ms, lower, upper)
        if len(Ms) == 0:
            raise Exception('Unexpected error: there are 0 intervals.')
        M = Ms
        i = i + 1
        print('Current limits: ' + str(M) + '\n')
    # Step 4: Computing the solution
    print('Step 4: Computing the solution.\n')
    m = M[0][0] % n
    print('Solution: ' + str(m) + '\n')
    return m
    
        
# %% Main

if __name__ == '__main__':
    print('\n\n\n')
    print("Bleichenbacher's PKCS 1.5 padding oracle attack: \n")
    print('\n\n\n')
    prime_size = 128
    plainText = b"kick it, CC"
    RSA = RSAPCKS1PaddingOracle(prime_size)
    print('Plain text to be encrypted: ' + str(plainText) + '\n')
    cipherText = RSA.encrypt(plainText)
    print('Cipher text to be sent over unsecure line: ' + str(cipherText) + '\n')
    print('Interecpting cipher text using man in the middle, received data:\n')
    public_key = RSA.send_public_key()
    print('Received public key: ' + str(public_key) + '\n')
    print('Received cipher text: ' + str(cipherText) + '\n')
    print('\n\n\n')
    sleep(10)
    recovered_plainText = Bleichenbacher_98_attack(cipherText, RSA)
    print('Actual plain text: ' + str(long_to_bytes(RSA.decrypt(cipherText),RSA.k)) + '\n')
    print('Recovered plain text: ' + str(long_to_bytes(recovered_plainText,RSA.k)) + '\n')
    print('Remove padding: \n')
    print('Actual plain text: ' + str(plainText) + '\n')
    print('Recovered plain text: ' + str(RSA.remove_pkcs(long_to_bytes(recovered_plainText))) + '\n')
    print('\n\n\n')
    





