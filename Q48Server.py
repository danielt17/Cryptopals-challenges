# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 23:58:11 2021

@author: danie
"""

# https://cryptopals.com/sets/4/challenges/32

# %% Imports

from Q47Utils import HMAC_SHA1,insecure_compare
from flask import Flask, request
from Crypto.Random import get_random_bytes
import numpy as np

# %% Functions

app = Flask(__name__)
@app.route('/test', methods=['GET'])
def login():
    if request.method == 'GET':
        file = request.args.get('file').encode()
        hashed = HMAC_SHA1(key, file).encode()
        signature = request.args.get('signature').encode()
        if insecure_compare(hashed, signature,sleepTime):
            return "OK", 200
        else:
            return "BAD", 500

# %% Main

if __name__ == '__main__':
    key = get_random_bytes(np.random.randint(1,128))
    sleepTime = 0.005
    app.run(port=8082)