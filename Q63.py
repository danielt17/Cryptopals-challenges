# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 20:10:03 2021

@author: danie
"""


# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:27:51 2021

@author: danie
"""

# https://cryptopals.com/sets/6/challenges/43

# %% Imports

from Q44 import SHA1
from Q51 import modexp
from Q57 import generate_prime_number,invmod,generate_prime_candidate
from random import randint,randrange
from tqdm import tqdm

# %% Functions
    
# miller rabin probalistic test for primality testing
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def miller_rabin_test(n,q,experiments = 128):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    if (n-1) % q != 0:
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

def generate_prime_number_given_condition(q,length=1024):
    p = 4 # intialize to something false with respect to miller rabin
    while not miller_rabin_test(p, q):
        p = generate_prime_candidate(length)
    return p

# implemenated using the description from wikipedia:
# https://en.wikipedia.org/wiki/Digital_Signature_Algorithm
class DSA:
    
    def __init__(self,generate_random_parameters):
        if generate_random_parameters:
            print('Generating parameters: \n')
            # SHA1 output length is 160 bits long there according to FIPS 186-4
            # one should use the following parameters: (L,N) = (1024,160)
            L = 1024; N = 160;
            self.q = generate_prime_number(N)
            self.p = generate_prime_number_given_condition(self.q,L)
            h = randint(2,self.p-2)
            self.g = modexp(h,(self.p-1)//self.q,self.p)
        else:
            print('Pre allocated parameters: \n')
            self.p = int('800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebeac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc871a584471bb1',16)
            self.q = int('f4f47f05794b256174bba6e9b396a7707e563c5b',16)
            self.g = int('5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119458fef538b8fa4046c8db53039db620c094c9fa077ef389b5322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a0470f5b64c36b625a097f1651fe775323556fe00b3608c887892878480e99041be601a62166ca6894bdd41a7054ec89f756ba9fc95302291',16)
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
        r = 0; s = 0;
        while r == 0:
            k = randint(1,self.q-1)
            r = modexp(self.g,k,self.p) % self.q
            while s == 0:
                s = (invmod(k,self.q) * (message_hash + private_key * r)) % self.q
        print('Generated message verifiers: \n')
        print('r: ' + str(r) + '\n')
        print('s: ' + str(s) + '\n')
        # usually we should not have access to k but for the first challange we need it
        return r,s,k
    
    def verify_message(self,message,r,s,public_key):
        print('Recieved: \n')
        print('Message: ' + str(message) + '\n')
        print('r: ' + str(r) + '\n')
        print('s: ' + str(s) + '\n')
        print('public_key: ' + str(public_key) + '\n')
        print('Verifing the message: \n')
        if (0 < r & r < self.q) & (0 < s & s < self.q):
            message_hash = int(SHA1(message),16)
            w = invmod(s,self.q)
            u1 = (message_hash * w) % self.q
            u2 = (r * w) % self.q
            v = ((modexp(self.g,u1,self.p)*modexp(public_key,u2,self.p)) % self.p) % self.q
            if v == r:
                print('Message verified \n')
            else:
                print('Message isnt verified \n')
        else:
            raise Exception('Invalid inputs, r and s arent within valid limits')
        
def attack_on_dsa_fixed_nonce(s,k,message_hash,r,q):
    estimated_private_key = (((s*k) - message_hash) * invmod(r,q)) % q
    return estimated_private_key

def brute_force_dsa_k_nonce(msg,r,s,public_key,p,q,g):
    print('Running brute force attack against DSA k nonce: \n')
    print('   1. we estimate the private key under fixed nonce assumption, where we loop over nonce k. \n')
    print('   2. we calculate the value of s and r. \n')
    print('   3. we compare the values of the s and r we calculated to the ones we were supplied. \n')
    print('We use this technique and not a direct calculation as it is a lot faster. \n')
    message_hash = int(SHA1(msg),16)
    for k in tqdm(range(2**16 + 1)):
        estimated_private_key = attack_on_dsa_fixed_nonce(s,k,message_hash,r,q)
        r_estimated = modexp(g,k,p) % q
        try:
            s_estimated = (invmod(k,q) * (message_hash + estimated_private_key * r_estimated)) % q
        except:
            continue
        if (r_estimated == r) & (s_estimated == s):
            return k,estimated_private_key
    raise Exception('Didn''t find private key')
        

# %% Main

if __name__ == '__main__':
    print('\n\n\n\n')
    print('DSA key recovery from nonce \n')
    print('\n\n')
    print('Part 1: implemenating DSA \n')
    dsa = DSA(False)
    message = b'GetZer0Dayed'
    private_key,public_key = dsa.generate_keys()
    r,s,k = dsa.sign_message(message,private_key)
    print('Sending message: ' + str(message) + '\n')
    print('Sending r,s, public key to user inorder to validate the message \n')
    dsa.verify_message(message,r,s,public_key)
    print('\n\n')
    print('Part 2: Attack 1 \n')
    print('Attack 1: recovering private key given known nonce k: \n')
    print('We know k = ' + str(k) + '\n')
    print('Recovering private key using the following calculation: ((s * k) - H(msg)/r) mod q \n')
    estimated_private_key = attack_on_dsa_fixed_nonce(s,k,int(SHA1(message),16),r,dsa.q)
    if private_key == estimated_private_key:
        print('Successful attack private key reocovered \n')
        print('Private key: ' + str(estimated_private_key) + '\n')
    else:
        print('Failed to recover private key, try again \n')
    print('\n\n')
    print('Part 3: Attack 2 \n')
    print('Attack 2: bad implementation of nonce k, k is limited between 1 to 2^16 therefore, brute force is possible \n')
    msg = b"For those that envy a MC it can be hazardous to your health\n" \
              b"So be friendly, a matter of life and death, just like a etch-a-sketch\n"
    if SHA1(msg) != "d2d0714f014a9784047eaeccf956520045c45265":
        raise Exception('Input string isnt formatted correctly \n')
    print('Message to be signed: ' + str(msg) + '\n')
    r = 548099063082341131477253921760299949438196259240
    s = 857042759984254168557880549501802188789837994940
    public_key = int('84ad4719d044495496a3201c8ff484feb45b962e7302e56a392aee4abab3e4bdebf2955b4736012f21a08084056b19bcd7fee56048e004e44984e2f411788efdc837a0d2e5abb7b555039fd243ac01f0fb2ed1dec568280ce678e931868d23eb095fde9d3779191b8c0299d6e07bbb283e6633451e535c45513b2d33c99ea17',16)
    print('Recieved s, r and public key: \n')
    print('r: ' + str(r) + '\n')
    print('s: ' + str(s) + '\n')
    print('public key: ' + str(public_key) + '\n')
    estimated_k,estimated_private_key_2 = brute_force_dsa_k_nonce(msg,r,s,public_key,dsa.p,dsa.q,dsa.g)
    print('\n')
    print('Estimated k: ' + str(estimated_k) + '\n')
    print('Estimated private key: ' + str(estimated_private_key_2) + '\n')
    if  SHA1(hex(estimated_private_key_2)[2:].encode()) == '0954edd5e0afe5542a4adf012611a91912a3ec16':
        print('Successfully got the flag! \n')
    else:
        print('Attack didnt fail, but there are problems with decoding the flag :( \n')
    
    
    
    
    
    