# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 19:43:42 2022
@author: danie
"""

# %% Imports

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.number import long_to_bytes
from Q28 import aes_cbc_encrypt
from Q46MD5 import MD5
from Q51 import run_diffie_hellman_exchange

# %% Functions

class Diffie_Hellman:
    
    def __init__(self):
        self.p = int('ffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff',16)
        self.g = 2
        
    def run_key_exchange(self):
        shared_secret = run_diffie_hellman_exchange(self.p,self.g)
        shared_secret_key = MD5(long_to_bytes(shared_secret)).digest()
        print('\n')
        print('Shared key: ' + str(shared_secret_key) + '.\n')
        return shared_secret_key

class AES_CBC_MAC:
    '''AES CBC MAC oracle'''
    
    def __init__(self,key,iv=None):
        # Initialize AES-CBC-MAC key and iv
        if iv is None:
            self.iv = get_random_bytes(AES.block_size)
        else:
            self.iv = iv
        self.key = key
        print('AES-CBC-MAC oracle is up, with the following parameters: \n')
        print('IV: ' + str(self.iv))
        print('Key: ' + str(self.key) + '\n')
    
    def get_mac(self,plainText):
        # Get MAC for plaintext
        cipherText = aes_cbc_encrypt(plainText,self.key,self.iv)
        mac = cipherText[-AES.block_size:]
        return mac

class Client:

    def __init__(self,key):
        self.from_id =  0
        self.to_id =  1
        self.Signing_Oracle = AES_CBC_MAC(key)
        
    def prepare_message(self,amount):
        if type(amount) != int:
            raise Exception("Message is not formatted correctly, make sure its an int!")
        message = 'from=#' + str(self.from_id) + '&to=#' + str(self.to_id) + '&amount=#' + str(amount)
        return message.encode()
    
    def send_message(self,amount):
        print('API got a request of sending: ' + str(amount) + str(' space bucks.\n'))
        message = self.prepare_message(amount)
        iv = self.Signing_Oracle.iv
        mac = self.Signing_Oracle.get_mac(message)
        full_message = dict({'message': message, 'iv': iv, 'mac': mac})
        print('Sent message: ' + str(full_message) + '\n')
        return full_message

class Server:
    
    def __init__(self,key, iv = None):
        self.key = key
        if iv is None:
            self.Verification_Oracle = None
        else:
            self.Verification_Oracle = AES_CBC_MAC(key,iv)

    def receive_and_validate_message(self,full_message):
        print('Received message: ' + str(full_message) + '\n')
        print('parsing the message: ')
        message = full_message['message']; iv = full_message['iv']; mac = full_message['mac']
        print('message: ' + str(message)); print('iv: ' + str(iv)); print('mac: ' + str(mac) + '\n')
        print('Signature verfication oracle is up: ')
        self.Verification_Oracle = AES_CBC_MAC(self.key,iv)
        if mac == self.Verification_Oracle.get_mac(message):
            print('Signature is valid!')
        else:
            print('Signature is invalid!!!!')
    
def failed_forgery(full_message,forged_amount=1000000):
    failed_forged_message = full_message.copy()
    failed_forged_message['message'] = (failed_forged_message['message'].decode()[:-3] + str(forged_amount)).encode()
    return failed_forged_message
    
    

# %% Main

if __name__ == '__main__':
    print('\n\n\n')
    print('CBC-MAC message forgery simulation:\n')
    key = Diffie_Hellman().run_key_exchange()
    client = Client(key)
    server = Server(key)
    full_message = client.send_message(500)
    print('First we will look at an example which has a valid signature: \n')
    server.receive_and_validate_message(full_message)
    print('Now we will look at an example which has an invalid signature and was fabricated badly: \n')
    forged_amount = 1000000
    failed_forged_message = failed_forgery(full_message,forged_amount)
    server.receive_and_validate_message(failed_forged_message)
    