# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 19:43:42 2022

@author: danie
"""

# %% Imports

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.number import long_to_bytes
from Q28 import aes_cbc_encrypt
from Q46MD5 import MD5
from Q51 import run_diffie_hellman_exchange

# %% Functions

class Diffie_Hellman:
    
    def __init__(self):
        self.p = int('ffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff',16)
        self.g = 2
        
    def run_key_exchange(self):
        shared_secret = run_diffie_hellman_exchange(self.p,self.g)
        shared_secret_key = MD5(long_to_bytes(shared_secret)).digest()
        print('Shared key: ' + str(shared_secret_key) + '.\n')
        return shared_secret_key

class AES_CBC_MAC:
    '''AES CBC MAC oracle'''
    
    def __init__(self,key):
        # Initialize AES-CBC-MAC key and iv
        self.iv = get_random_bytes(AES.block_size)
        self.key = key
        print('AES-CBC-MAC oracle is up, with the following parameters: \n')
        print('IV: ' + str(self.iv))
        print('Key: ' + str(self.key) + '\n')
    
    def get_new_iv(self):
        self.iv = get_random_bytes(AES.block_size)
    
    def get_mac(self,plainText):
        # Get MAC for plaintext
        cipherText = aes_cbc_encrypt(plainText,self.key,self.iv)
        mac = cipherText[-AES.block_size:]
        return mac

# %% Main

if __name__ == '__main__':
    print('\n\n\n')
    print('CBC-MAC message forgery simulation:\n')
    key = Diffie_Hellman().run_key_exchange()
    Oracle = AES_CBC_MAC(key)