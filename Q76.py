# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 18:02:14 2023

@author: danie
"""

# %% Imports

from Q75 import md
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from dataclasses import dataclass
from numpy import ceil
from tqdm import tqdm

# %% Find collision function

def find_collision(H1, H1_len, H2, H2_len):
    # Finding a collision between two states of the length
    if H1_len != H2_len:
        raise Exception("Both states must have the same length")
    
    n = H1_len//2 * 8 
    digests = {}
    while True:
        # constructing 2^(n/2) message from H1
        for _ in range(n):
            msg1 = get_random_bytes(AES.block_size)
            msg1_len = len(msg1)
            msg1_digest = md(msg1, msg1_len, H1, H1_len, enb_len_padding=False)
            digests[msg1_digest] = msg1
        # constructing 2^(n/2) message from H2
        for _ in range(n):
            msg2 = get_random_bytes(AES.block_size)
            msg2_len = len(msg2)
            msg2_digest = md(msg2, msg2_len, H2, H2_len, enb_len_padding=False)
            # check for a collision
            if msg2_digest in digests:
                m1 = digests[msg2_digest]
                m2 = msg2
                digest = msg2_digest
                return m1, m2, digest

# %% Building a diamond structure as described in the paper: Kelsey and Kohno's Nostradamus Attack.
# link here: https://eprint.iacr.org/2005/281


# create a diamond structure node class

@dataclass
class Node:
    state: bytes
    next_node = None
    msg = None

# creating the diamond structure

def diamond_structure(k, H_len):
    # starting by initializing 2**k hash values in each node
    initial_states = [Node(get_random_bytes(H_len)) for _ in range(2**k)]
    # updating state list
    state_list = initial_states
    # Building each level of the tree on after another
    for _ in tqdm(range(k),desc="Building diamond structure"):
        next_state_list = []
        # each pair of states creates a single collision block
        for cur_state_ind in range(0,len(state_list),2):
            node1, node2 = state_list[cur_state_ind], state_list[cur_state_ind+1]
            node1_len, node2_len = len(node1.state), len(node2.state)
            m1, m2, digest = find_collision(node1.state, node1_len, node2.state, node2_len)
            # updating the diamond tree nodes
            new_node = Node(digest)
            next_state_list.append(new_node)
            node1.msg, node2.msg = m1, m2
            node1.next_node, node2.next_node = new_node, new_node
            
        # update node lisst for next level
        state_list = next_state_list
        
    return initial_states, state_list[0].state

           
# %% Nostradamus attack

class Nostradamus:
    # Preforming the Nostradamus attack
    def __init__(self, k, H, H_len, max_msg_blocks):
        # Initialize parameters and diamond structure
        self.k = k
        self.H = H
        self.H_len = H_len
        self.max_msg_blocks = max_msg_blocks
        self.diamond_leaves, self.root_state = diamond_structure(self.k, self.H_len)
        
    def get_digest(self):
        # get digest at the root of the diamond structure
        prediction_len = (self.max_msg_blocks + 1 + self.k) * AES.block_size
        padding_block = prediction_len.to_bytes(AES.block_size, 'big')
        # find digest
        digest = md(padding_block, len(padding_block), self.root_state, len(self.root_state), enb_len_padding=False)
        return digest
    
    def generate_ctfp(self, prefix: bytes):
         """ Generate a prediction containing given [prefix] """
         # validate prefix max length
         if ceil(len(prefix) / AES.block_size) > self.max_msg_blocks:
             raise ValueError('prefix is too long')
         # pad the prefix to match multiply of block size
         reminder = len(prefix) % AES.block_size
         if reminder > 0:
             prefix += bytes(AES.block_size - reminder)
         # find collision with one of the tree leaves
         prefix_digest = md(prefix, len(prefix), self.H, self.H_len, enb_len_padding=False)
         while True:
             link_msg = get_random_bytes(AES.block_size)
             cur_hash = md(link_msg,len(link_msg), prefix_digest, self.H_len, enb_len_padding=False)
    
             leaf = next((x for x in self.diamond_leaves if x.state == cur_hash), None)
             if leaf is not None:
                 break
         # build message
         msg = prefix + link_msg
         cur_node = leaf
         while cur_node.next_node is not None:
             msg += cur_node.msg
             cur_node = cur_node.next_node
    
         return msg

# %% Main

def main():
    print("Preforming the Nostradamus attack\n")
    # Initial global varibles
    k = 9       # number of levels in diamond strcuture
    H_len = 4   # state size in bytes
    H = get_random_bytes(H_len)
    max_msg_blocks = 2
    # create proof of a secret prediction
    nostradamus = Nostradamus(k, H, H_len, max_msg_blocks)
    known_digest = nostradamus.get_digest()
    print(f'Known digest: {known_digest}\n')
    # generate ctpf
    challenger_prefix = b'There will be a War in 2020'
    prediction = nostradamus.generate_ctfp(challenger_prefix)
    print(f'Prediction: {prediction}\n')
    # Proof
    prediction_digest = md(prediction, len(prediction), H, H_len)
    print(f'Prediction digest: {prediction_digest}\n')
    if prediction_digest == known_digest:
        print("Successful prediction!\n")
    

# %% Run main

if __name__ == "__main__":
    main()