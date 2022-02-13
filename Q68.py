# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 19:20:49 2022

@author: danie
"""


# https://cryptopals.com/sets/6/challenges/48

# %% Imports

from Q67 import RSAPCKS1PaddingOracle,Bleichenbacher_98_attack
from Crypto.Util.number import long_to_bytes
import sys
from time import sleep
from pwn import hexdump

sys.setrecursionlimit(1500)

# %% Main

if __name__ == '__main__':
    print('\n\n\n')
    print("Bleichenbacher's PKCS 1.5 padding oracle attack: \n")
    print('\n\n\n')
    prime_size = 1024
    plainText = b"kick it, CC"
    RSA = RSAPCKS1PaddingOracle(prime_size)
    print('Plain text to be encrypted: ' + str(plainText) + '\n')
    cipherText = RSA.encrypt(plainText)
    print('Cipher text to be sent over unsecure line: ' + str(cipherText) + '\n')
    print('Interecpting cipher text using man in the middle, received data:\n')
    public_key = RSA.send_public_key()
    print('Received public key: ' + str(public_key)+ '\n')
    print('Received cipher text: ' + str(cipherText) + '\n')
    print('\n\n\n')
    sleep(10)
    recovered_plainText = Bleichenbacher_98_attack(cipherText, RSA)
    print('Actual plain text: \n')
    print(hexdump(long_to_bytes(RSA.decrypt(cipherText),RSA.k)) + '\n')
    print('Recovered plain text: \n')
    print(hexdump(long_to_bytes(recovered_plainText,RSA.k)) + '\n')
    print('Remove padding: \n')
    print('Actual plain text: ' + str(plainText) + '\n')
    print('Recovered plain text: ' + str(RSA.remove_pkcs(long_to_bytes(recovered_plainText))) + '\n')
    print('\n\n\n')
    
        
    
    
    