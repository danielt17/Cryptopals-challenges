# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 22:50:13 2021

@author: danie
"""


# https://cryptopals.com/sets/5/challenges/39

# %% Imports

from random import randrange, getrandbits
from Q51 import modexp

# %% Functions

# extended euclidain algorithm
# https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
def egcd(a,b):
    if a == 0:
        return (b,0,1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x- (b//a) * y, y)
    
# modular multiplicative inverse
# https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
def invmod(a,m):
    g, x, y = egcd(a,m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# miller rabin probalistic test for primality testing
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def miller_rabin_test(n,experiments = 128):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    for _ in range(experiments):
        a = randrange(2, n - 1)
        x = modexp(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = modexp(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False    
    return True

def generate_prime_candidate(length):
    p = getrandbits(length)
    # 1024 bit by MSB and make sure its odd by setting LSB to 1
    p = p | ((1 << length - 1) | 1)
    return p
    
def generate_prime_number(length=1024):
    p = 4 # intialize to something false with respect to miller rabin
    while not miller_rabin_test(p, 128):
        p = generate_prime_candidate(length)
    return p
    

def rsa(plainText,print_procedure = False):
    print('RSA algorithm implementation: \n')
    succed_in_suitable_primes = False # we need phi_n to be coprime to e therefore looping until we find suitable primes for this condition
    while not succed_in_suitable_primes:
        try:
            p = generate_prime_number()
            q = generate_prime_number()
            n = p * q
            phi_n = (p-1) * (q-1) # if p is prime the number of euler totient function is p -1 as all the numbers below p are coprime to p,  the multiplcation is done because the totient function is multiplicative
            e = 3
            d = invmod(e,phi_n)
            succed_in_suitable_primes = True
        except:
            continue
    public_key = (e,n)
    private_key = (d,n)
    cipherText = modexp(plainText, public_key[0], public_key[1])
    plainTextRecovered = modexp(cipherText, private_key[0], private_key[1])
    if print_procedure:
        print('Generating primes: \n')
        print('p: ' + str(p) + '\n')
        print('q: ' + str(q) + '\n')
        print('n: ' + str(n) + '\n')
        print('et: ' + str(phi_n) + '\n')
        print('e: ' + str(e) + '\n')
        print('d: ' + str(d) + '\n')
        print('Public key: ' + str(public_key) + '\n')
        print('Private key: ' + str(private_key) + '\n')
        print('Plain text: ' + str(plainText) + '\n')
        print('Cipher text: ' + str(cipherText) + '\n')
        print('Recovered plain text: ' + str(plainTextRecovered) + '\n')
    return plainTextRecovered

def str_to_num_for_rsa(string):
    return int(string.encode().hex(),16)

def num_to_str_for_rsa(number):
    return bytes.fromhex(hex(number)[2:]).decode()

# %% Main

if __name__ == '__main__':
    plainText = 42
    rsa(plainText,print_procedure = True)
    plainText = 'Hello there!'
    print('\n \n \n \n \n \n')
    print('Plain text: ' + str(plainText) + '\n')
    recovredText = rsa(str_to_num_for_rsa(plainText),print_procedure = True)
    print('Plain text: ' + str(num_to_str_for_rsa(recovredText)) + '\n')
    
    
    