# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 13:43:52 2021

@author: danie
"""

# https://cryptopals.com/sets/2/challenges/15

# %% Imports

import numpy as np

# %% Functions

def cheack_valid_padding(textpadded):
    padding_value = textpadded[-1]
    if (len(textpadded[:-textpadded[-1]]) + padding_value) == len(textpadded):
        arr = np.array(list(textpadded[-textpadded[-1]:]))
        if sum(arr == padding_value) == padding_value:
            return True
        else:
            return False
    else:
        return False

def unpadding_without_blocksize(textpadded):
    if cheack_valid_padding(textpadded):
        return textpadded[:-textpadded[-1]]
    else:
        return 'Invalid padding'

# %% Main

if __name__ == '__main__':
    string1 = b"ICE ICE BABY\x04\x04\x04\x04"
    string2 = b"ICE ICE BABY\x05\x05\x05\x05"
    string3 = b"ICE ICE BABY\x01\x02\x03\x04"
    print('For string: ' + str(string1) + ' we expect valid padding, our algorithm returns: ' + str(unpadding_without_blocksize(string1)))
    print('For string: ' + str(string2) + ' we expect invalid padding, our algorithm returns: ' + str(unpadding_without_blocksize(string2)))
    print('For string: ' + str(string3) + ' we expect invalid padding, our algorithm returns: ' + str(unpadding_without_blocksize(string3)))
