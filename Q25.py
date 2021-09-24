# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 19:22:48 2021

@author: danie
"""


# %% Challange

# https://cryptopals.com/sets/2/challenges/13

# %% Imports

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Q22 import aes_ecb_encrypt_padded,aes_ecb_decrypt_padded

# %% Functions

def k_v_encode(kv_dict):
    string = ''
    for element in kv_dict.items():
        key = element[0]; value = element[1]
        string = string + str(key) + '=' + str(value) + '&' 
    return string[:-1]

def k_v_parse(string):
    elements = string.split('&')
    parsed = {}
    for element in elements:
        cur = element.split('=')
        parsed[cur[0]] = cur[1]
    return parsed

def profile_for(email):
    email = email.replace('&', '').replace('=', '')
    parsed = {'email': email,'uid': 10,'role': 'user'}   
    return parsed

class AesEcbOracle:
    def __init__(self):
        self.key = get_random_bytes(AES.block_size)
        
    def encrypt(self,email):
        encodedUserProfile = k_v_encode(profile_for(email)).encode()
        return aes_ecb_encrypt_padded(encodedUserProfile,self.key)
        
    def decrypt(self, cipherText):
        return k_v_parse(aes_ecb_decrypt_padded(cipherText,self.key).decode())

def cut_and_paste_attack(Oracle):
    emailLen = AES.block_size - len(b'email=')
    ruleLen = AES.block_size - len(b'admin')
    email1 = "x" * emailLen + "admin" + (chr(ruleLen) * ruleLen)
    encrypt1 = Oracle.encrypt(email1)
    email2 = "eat@shitt.com"
    encrypt2 = Oracle.encrypt(email2)
    # (block1(enc2) = email=eat@shitt.) + (block2(enc2) = com&uid=10&role=) + (block2(enc1) = admin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b) 
    # Bits requests: b'email=eat@shitt.com&uid=10&role=admin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b' (Ending for valid padding)
    forced = encrypt2[:32] + encrypt1[16:32]
    return forced

# %% Main

if __name__ == '__main__':
    email = "foo@bar.com"
    Oracle = AesEcbOracle()
    cipherText = Oracle.encrypt(email)
    expectedPlainText = Oracle.decrypt(cipherText)
    cutAndPastePlainText = Oracle.decrypt(cut_and_paste_attack(Oracle))
    if cutAndPastePlainText['role'] == 'admin':
        print('Successful access')
    else:
        print('You didnt gain access')
    