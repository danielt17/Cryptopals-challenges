# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 16:00:35 2021

@author: danie
"""

# https://cryptopals.com/sets/5/challenges/40

# %% Imports

from Q51 import modexp
from Q57 import generate_prime_number,invmod,str_to_num_for_rsa,num_to_str_for_rsa
import sys
sys.setrecursionlimit(1500)

# %% Functions

class RSAOracle:
    
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
        
    def send_public_key(self):
        return self.public_key
        
    def encrypt(self,plainText,public_key=None):
        if public_key is None:
            public_key = self.public_key
        return modexp(str_to_num_for_rsa(plainText), public_key[0], public_key[1])

    def decrypt(self,cipherText):
        return num_to_str_for_rsa(modexp(cipherText, self.private_key[0], self.private_key[1]))

# https://stackoverflow.com/questions/55436001/cube-root-of-a-very-large-number-using-only-math-library
def find_invpow(x,n):
    # finds nth root of x using binary search
    high = 1
    while high ** n < x:
        high *= 2
    low = high//2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1

def e_3_rsa_broadcast_attack(plainText):
    print('Running encryption oracles (it takes a bit of time for primes of 1024 bits size): \n')
    Oracle1 = RSAOracle(); rx1 = [Oracle1.send_public_key(), Oracle1.encrypt(plainText)];
    print('Recived data from Oracle 1: e = ' + str(rx1[0][0]) + ', n = ' + str(rx1[0][1]) + ', cipher text = '  + str(rx1[1]) + '\n')
    Oracle2 = RSAOracle(); rx2 = [Oracle2.send_public_key(), Oracle2.encrypt(plainText)];
    print('Recived data from Oracle 2: e = ' + str(rx2[0][0]) + ', n = ' + str(rx2[0][1]) + ', cipher text = '  + str(rx2[1]) + '\n')
    Oracle3 = RSAOracle(); rx3 = [Oracle3.send_public_key(), Oracle3.encrypt(plainText)];
    print('Recived data from Oracle 3: e = ' + str(rx3[0][0]) + ', n = ' + str(rx3[0][1]) + ', cipher text = '  + str(rx3[1]) + '\n')
    print('Running E=3 rsa broadcast attack (using chinese remainder theorem): \n')
    # Chinese remainder theorem https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html
    n1 = rx1[0][1]; n2 = rx2[0][1]; n3 = rx3[0][1];
    c1 = rx1[1]; c2 = rx2[1]; c3 = rx3[1];
    N = n1 * n2 * n3;  m1 = n2 * n3; m2 = n1 * n3; m3 = n1 * n2;
    result = (c1 * m1 * invmod(m1,n1) + c2 * m2 * invmod(m2,n2) + c3 * m3 * invmod(m3,n3)) % N
    recovered_plainText = find_invpow(result,3)
    return num_to_str_for_rsa(recovered_plainText)
    

# %% Main

if __name__ == '__main__':
    print('\n \n \n')
    print('E=3 rsa broadcast attack simulation: \n')
    plainText = 'Hello there!'
    print('Plain text: ' + plainText + '\n')
    recovered_plainText = e_3_rsa_broadcast_attack(plainText)
    print('Recovered plain text: ' + recovered_plainText + '\n')