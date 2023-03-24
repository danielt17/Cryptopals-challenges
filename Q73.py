# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 13:38:09 2023

@author: danie
"""

# %% Imports

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from zlib import compress, decompress
from Q32 import aes_ctr
import string
import numpy as np

# %% Compression oracle

class CompressionOracle:
    
    def __init__(self):
        self.request_method = "POST / HTTP/1.1"
        self.host = "hapless.com"
        self.cookie = "sessionid=TmV2ZXIgcmV2ZWFsIHRoZSBXdS1UYW5nIFNlY3JldCE="
    
    def format_request(self,choosen_plaintext):
        message = f"{self.request_method}\nHost: {self.host}\nCookie: {self.cookie}\n"\
                  f"Content-Length: {len(choosen_plaintext)}\nMessage: {choosen_plaintext}"
        return message
    
    def compress_message(self,message):
        compressed_message = compress(message.encode())
        return compressed_message
        
    def encrypt(self,choosen_plaintext):
        self.key = get_random_bytes(AES.block_size)
        self.nonce = int.from_bytes(get_random_bytes(AES.block_size//2),"big")
        self.message = self.format_request(choosen_plaintext)
        self.compressed_message = self.compress_message(self.message)
        self.ciphertext = aes_ctr(self.compressed_message,self.key,self.nonce)
        self.ciphertext_len = len(self.ciphertext)
        
    def decrypt(self,ciphertext):
        decrypted_compressed_message = aes_ctr(ciphertext,self.key,self.nonce)
        recovered_message = decompress(decrypted_compressed_message).decode()
        return recovered_message
        
# %% Attack    

def crime_attack(oracle):
    """
    The attack is based upon the following paper:
        https://www.iacr.org/cryptodb/archive/2002/FSE/3091/3091.pdf
    and presentation:
        https://docs.google.com/presentation/d/11eBmGiHbYcHR9gL5nDyZChu_-lCa2GizeuOfaLU2HOU/edit#slide=id.g1d134dff_1_222

    """
    attack_message = "sessionid="
    oracle.encrypt(attack_message)
    initial_len = oracle.ciphertext_len
    possible_ascii = string.printable
    while "\n" not in attack_message:
        length_ratios = [];
        for cur_ind in range(len(possible_ascii)):
            cur_candidate = possible_ascii[cur_ind]
            oracle.encrypt(attack_message + cur_candidate)
            cur_len = oracle.ciphertext_len
            len_ratio = cur_len/initial_len
            length_ratios.append(len_ratio)
        best_candidate = possible_ascii[np.argmin(length_ratios)]
        attack_message = attack_message + best_candidate
    return attack_message[:-1]
            
# %% Main

def main():
    oracle = CompressionOracle()
    oracle.encrypt("")
    recovered_message = oracle.decrypt(oracle.ciphertext)
    if recovered_message != oracle.message:
        raise Exception("Implementation of compression oracle isn't correct, fix it!")
    attack_message = crime_attack(oracle)
    if attack_message == oracle.cookie:
        print(f"Succesfully recovered the cookie.\nOriginal cookie: {oracle.cookie}\nEstimted cookie by attack: {attack_message}")
    else:
        raise Exception(f"Attack failed!")

# %% Run main

if __name__ == "__main__":
    main()
