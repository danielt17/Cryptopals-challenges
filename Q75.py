# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 16:28:09 2023

@author: danie
"""

# %% Imports

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import random
import numpy as np
from tqdm import tqdm

# %% Merkle-Damgard Hash function construction using AES with length extension padding

def md(msg, msg_len, H, H_len, enb_len_padding=True):
    # standard length padding to equal block size
    remainder_len = msg_len % AES.block_size
    if remainder_len > 0:
        msg = msg + b"\x80" 
        msg = msg + bytes(AES.block_size - remainder_len - 1) # zero bytes padding
    # Padding againt length extension attacks
    if enb_len_padding:
        msg = msg + msg_len.to_bytes(AES.block_size,"big")
    # Produce digest Merkle-Damgard construction using keyed AES
    for i in range(0,len(msg),AES.block_size):
        H = H + bytes(AES.block_size - len(H))
        m_block = msg[i:i+AES.block_size]
        H = AES.new(H,AES.MODE_ECB).encrypt(m_block)
        H = H[:H_len]
    return H

# %% Expandable message construction

class Expandable_Message:
    
    def __init__(self, k, H):
        # Initializing the expandable message class parameters
        self.k = k
        self.H = H
        self.msg_ls = []
        self.cur_H = self.H
       
    def find_collision(self,H, k, j):
        # Finds a collsion between a single block message and a message of 2**(k-1)+1 blocks
        n = 8*len(H)
        single_block_digest_dict = {}
        while True:
            # Constructing approximately 2**(n/2) messages of length 1
            for _ in range(n//2 + 1):
                msg = get_random_bytes(AES.block_size)
                msg_digest = md(msg,AES.block_size,H,len(H),enb_len_padding=False)
                single_block_digest_dict[msg_digest] = msg
            # Finding collision between a single block length msg and a message of length 2**(k-j)+1
            length_prefix = get_random_bytes(AES.block_size * (2**(k-j)))
            length_prefix_digest = md(length_prefix,len(length_prefix),H,len(H),enb_len_padding=False)
            # look at the result of the last hash block and check for a collsion
            for _ in range(n//2 + 1):
                last_block = get_random_bytes(AES.block_size)
                last_block_digest = md(last_block,len(last_block),length_prefix_digest,len(length_prefix_digest),enb_len_padding=False)
                if last_block_digest in single_block_digest_dict:
                    m1 = single_block_digest_dict[last_block_digest]
                    m2 = length_prefix + last_block
                    digest_final = last_block_digest
                    # Check that actually we have the correct parameters
                    assert len(m1) == AES.block_size
                    assert len(m2) == AES.block_size * (2 ** (k-j) + 1)
                    assert md(m1, len(m1), H, len(H), enb_len_padding=False) == digest_final
                    assert md(m2, len(m2), H, len(H), enb_len_padding=False) == digest_final
                    return m1, m2, digest_final
    
    def create_msg_ls(self):
        # Create messages of different lengths coliding with a single message block
        temp_H = self.cur_H
        for j in tqdm(range(1,self.k+1), desc = "Create messages list of collisions of diffreent lengths with single block message"):
            m1, m2, temp_H = self.find_collision(temp_H, self.k, j)
            self.msg_ls.append((m1,m2))
        self.cur_H = temp_H
        return self.msg_ls
    
    def generate_expandable_message_prefix(self, n_blocks):
        # This function generates prefixes for expandable messages
        if n_blocks < self.k or (self.k + 2**self.k - 1) < n_blocks:
            raise Exception("Number of blocks is out of bounds, please check attack requirements")
        n_blocks_to_add = n_blocks - self.k
        seq = [1 if digit == "1" else 0 for digit in format(n_blocks_to_add, f'0{self.k}b')]
        msg = b''.join([block[seq[idx]] for idx, block in enumerate(self.msg_ls)])
        # Validate message length
        assert len(msg)/AES.block_size == n_blocks
        return msg
        
# %% Preimage attack based on Expandable Message

def preimage_attack(msg, msg_len, H, H_len):
    # Create expandable messages
    k = np.int64(np.floor(np.log2(msg_len/AES.block_size)))
    expandable_message = Expandable_Message(k, H)
    _ = expandable_message.create_msg_ls()
    expandable_message_digest = expandable_message.cur_H
    # generate a map of intermediate hash states to the block indices that they correspond to
    digests = {}
    cur_H = H
    for i in range(0, msg_len, AES.block_size):
        # Pad H to key size of AES
        cur_H = cur_H + bytes(AES.block_size - len(cur_H))
        # preform hashing til point
        msg_block = msg[i:i+AES.block_size]
        if len(msg_block) != AES.block_size:
            break
        cur_H = AES.new(cur_H, AES.MODE_ECB).encrypt(msg_block)
        cur_H = cur_H[:H_len]
        # add new state
        if (k-1)*AES.block_size <= i:
            digests[cur_H] = i
    # Find a single bridge block to intermediate state in the mapping
    while True:
        bridge_block = get_random_bytes(AES.block_size)
        next_H = md(bridge_block,AES.block_size,expandable_message_digest,H_len, enb_len_padding=False)
        if next_H in digests:
            suffix_idx = digests[next_H] + AES.block_size
            break
    # generate a prefix of the right length such that it has the same length as M
    suffix = msg[suffix_idx:]
    prefix_len = (msg_len-len(suffix))//AES.block_size - 1
    prefix = expandable_message.generate_expandable_message_prefix(prefix_len)
    # generate the fake message
    fake_msg = prefix + bridge_block + suffix
    fake_msg_digest = md(fake_msg, len(fake_msg), H, H_len)
    # Check validity of procedure
    assert len(fake_msg) == msg_len
    assert md(msg, msg_len , H, H_len) == fake_msg_digest
    return fake_msg, fake_msg_digest
    
# %% Main

def main():
    # Create random messge
    k = 8
    byte_offset = random.randint(0,AES.block_size)
    msg_len = AES.block_size * (2 ** k) + byte_offset
    msg = get_random_bytes(msg_len)
    # Produce initial state
    H_len = 4 
    H = get_random_bytes(H_len)
    # Produce message digest
    msg_digest = md(msg, msg_len, H, H_len, enb_len_padding=True)
    # Preimage attack
    fake_msg, fake_msg_digest = preimage_attack(msg, msg_len, H, H_len)
    if fake_msg_digest == msg_digest:
        print("Found successfully a preimage using Expandable Message attack by Kelsey and Schneier's")
    
    

# %% Run main

if __name__ == "__main__":
    main()
