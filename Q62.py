# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:27:51 2021

@author: danie
"""

# https://cryptopals.com/sets/6/challenges/42

# %% Imports

from Q44 import SHA1
from Q51 import modexp
from Q57 import generate_prime_number,invmod
from Q58 import find_invpow
from binascii import unhexlify
import re
import base64

# %% Functions

class RSA:
    
    def __init__(self):
        self.succeed_in_suitable_primes = False
        while not self.succeed_in_suitable_primes:
            try:
                self.p = generate_prime_number()
                self.q = generate_prime_number()
                self.n = self.p * self.q
                self.phi_n = (self.p-1) * (self.q-1)
                self.e = 3
                self.d = invmod(self.e,self.phi_n)
                self.succeed_in_suitable_primes = True
            except:
                continue
        self.public_key = [self.e,self.n]
        self.private_key = [self.d,self.n]
        
    def send_public_key(self):
        return self.public_key
        
    def encrypt(self,plainText):
        return modexp(plainText, self.public_key[0], self.public_key[1])

    def decrypt(self,cipherText):
        return modexp(cipherText, self.private_key[0], self.private_key[1])

# Taken from here https://stackoverflow.com/questions/21017698/converting-int-to-bytes-in-python-3
def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def bytes_to_int(x):
    return int.from_bytes(x, 'big')

def int_to_base64(x):
    # x in bytes
    return str(base64.b64encode(x))[2:-1]

def print_certificate(signature):
    # encrypted_signature in bytes
    print('-----BEGIN CERTIFICATE-----')
    print(int_to_base64(signature))
    print('-----END CERTIFICATE-----\n')

class RSADigitalSignature():
    
    def __init__(self):
        # ASN1 value taken from RFC-3447 
        # https://datatracker.ietf.org/doc/html/rfc3447#page-43
        self.RSAClass = RSA()
        self.ASN1_SHA1 = b'\x30\x21\x30\x09\x06\x05\x2b\x0e\x03\x02\x1a\x05\x00\x04\x14'
        print('Digital signture algorithm is up and running\n')
    
    def sign(self,message):
        # message is a bytes object
        # amount of \xff is defined here https://datatracker.ietf.org/doc/html/rfc3447#page-42
        emLen = 128 - len(self.ASN1_SHA1) # output will be 1024 bits = 128 octets
        tLen = 20 # 20 from sha1 output length
        numFF = emLen - tLen - 3 # 2 from start, 1 from before ASN1
        signature = b'\x00\x01' + b'\xff'*numFF + b'\x00'+ self.ASN1_SHA1 + unhexlify(SHA1(message))
        return self.RSAClass.decrypt(bytes_to_int(signature))
    
    def verify_signature(self,message,encrypted_signature):
        # encrypted_signature is an int object
        signature = b'\x00' + int_to_bytes(self.RSAClass.encrypt(encrypted_signature)) # \x00 isnt present so we add it
        print('Decrypted certificate: \n')
        print_certificate(signature)
        r = re.compile(b'\x00\x01\xff+?\x00.{15}(.{20})', re.DOTALL)
        m = r.match(signature)
        if not m:
            return False
        return m.group(1) == unhexlify(SHA1(message))
    
    def print_verify_signature(self,message,encrypted_signature):
        valid_result = self.verify_signature(message,encrypted_signature)
        if valid_result:
            print('Signature is valid\n')
        else:
            raise Exception('Signature is invalid!')
        
# Attack taken from here https://mailarchive.ietf.org/arch/msg/openpgp/5rnE9ZRN1AokBVj3VqblGlP63QE/  
def forge_signature(message_to_be_forged,key_length = 1024):
    ASN1_SHA1 = b'\x30\x21\x30\x09\x06\x05\x2b\x0e\x03\x02\x1a\x05\x00\x04\x14'
    block_format = b'\x00\x01\xff\x00' + ASN1_SHA1 + unhexlify(SHA1(message_to_be_forged))
    garbage = b'\xff'+ b'\x00' * (key_length//8-len(block_format)) # have to add at the start something other than \x00 because for some very odd reason it desregard the next numbers otherwise
    block_format =  block_format + garbage
    pre_encryption = bytes_to_int(block_format)
    forged_signature = find_invpow(pre_encryption,3)
    print('Forged encrypted signature: \n')
    print_certificate(int_to_bytes(forged_signature))
    return forged_signature

# %% Main

if __name__ == '__main__':
    print('\n\n')
    print("Bleichenbacher's e=3 RSA Attack on a digital certificate \n")
    print('First we will look at the creation of a valid certificate: \n')
    DSA = RSADigitalSignature()
    message = b'Hello there!'
    print('Message: ' + str(message) + '\n')
    encrypted_signature = DSA.sign(message)
    print('Encrypted certificate: \n')
    print_certificate(int_to_bytes(encrypted_signature))
    DSA.print_verify_signature(message,encrypted_signature)
    print('\n\n')
    message_to_be_forged = b'GeT ZeR0 DaYeD'
    print('We want to forge a certificate for the following messagae: ' + str(message_to_be_forged) + '\n')
    forged_signature = forge_signature(message_to_be_forged)
    print('Checking if our forged signature passes as a valid signature: \n')
    DSA.print_verify_signature(message_to_be_forged,forged_signature)
    print('Successfully forged a signature for the message: ' + str(message_to_be_forged))
    
    
    