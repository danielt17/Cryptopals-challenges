# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 22:27:25 2021

@author: danie
"""

# https://cryptopals.com/sets/4/challenges/31

# %% Imports

import requests
from time import time
from tqdm import tqdm
import numpy as np

# %% Functions

def send_request_get_response(fileName,signature):
    start = time()
    response = requests.get('http://localhost:8082/test?file=' + fileName + '&signature=' + signature)
    end = time()
    return response.status_code,end - start

def time_leak_side_channel_attack(fileName,numExperiments):
    signatureLength = 40 # 160 bits -> 20 bytes SHA1 hash output (40 in hex)
    signature = ''
    for i in tqdm(range(signatureLength)):
        timeArray = [0] * 16
        print('\n')
        print('Estimating byte number: ' + str(i + 1))
        for j in range(16):
            curSignature = signature + hex(j)[-1]
            print('Current signature progress: ' + str(curSignature))
            for experiment in range(numExperiments):
                response, estimatedTime = send_request_get_response(fileName,curSignature)
                timeArray[j] = timeArray[j] + estimatedTime
            timeArray[j] = timeArray[j]/numExperiments
        nextByte = np.argmax(np.array(timeArray))
        signature = signature + hex(nextByte)[-1]
    if send_request_get_response(fileName,signature)[0] == 200:
        print('File HMAC recovered')
    else:
        raise Exception('Time leakage attack failed')
    return signature
        
# %% Main

if __name__ == '__main__':
    fileName = 'GetZeroDayed'
    numExperiments = 1
    estimatedHMACSigniture = time_leak_side_channel_attack(fileName,numExperiments)
    print('File name: ' + fileName + ' . Estimated HMAC: ' + str(estimatedHMACSigniture))