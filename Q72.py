# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 16:18:06 2022

@author: danie
"""


# %% Imports

from Crypto.Cipher.AES import block_size
from Q71IVcontrol import AES_CBC_MAC
from Crypto.Util.Padding import pad
from Q22 import xor
from pwn import hexdump

# %% Functions

def find_collision(forged_file,fake_file_hash,original_file,target_hash,Hashing_Oracle):
    p1 = pad(forged_file,block_size);
    p2 = xor(fake_file_hash,original_file[:block_size])
    p3 = original_file[block_size:]
    new_forged_file = p1 + p2 + p3
    fake_file_forged_hash = Hashing_Oracle.get_mac(new_forged_file)
    return new_forged_file,fake_file_forged_hash
    
# %% Main

if __name__ == '__main__':
    print('\n')
    print('Find a collision in CBC-MAC hashing\n')
    key = b"YELLOW SUBMARINE"
    iv = bytearray([0]*16)
    Hashing_Oracle = AES_CBC_MAC(key,iv)
    original_file = b"alert('MZA who was that?');"
    original_file_hash = Hashing_Oracle.get_mac(original_file)
    print('Original file content: \n' + str(hexdump(original_file)) + '\n')
    print('Original file hash: \n' + str(hexdump(original_file_hash)) + '\n')
    forged_file = b"alert('Ayo, the Wu is back!');"
    fake_file_hash = Hashing_Oracle.get_mac(forged_file)
    print('Fake file content: \n' + str(hexdump(forged_file)) + '\n')
    print('Fake file original hash: \n' + str(hexdump(fake_file_hash)) + '\n')
    print('\n\nWe want to get the fake file to have the same hash as the original file, we will use a length extension attack:\n')
    new_forged_file,fake_file_forged_hash = find_collision(forged_file,fake_file_hash,original_file,target_hash=original_file_hash,Hashing_Oracle=Hashing_Oracle)
    print('New forged file content: \n' + str(hexdump(new_forged_file)) + '\n')
    print('New forged file hash: \n' + str(hexdump(fake_file_forged_hash)) + '\n')
    if fake_file_forged_hash == original_file_hash:
        print('Foundd successfully a hash collision!\n')
    else:
        print('Failed to find a hash collision!\n')
    
    
    