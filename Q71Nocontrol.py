# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 17:27:59 2022

@author: danie
"""

# %% Imports

from Crypto.Cipher.AES import block_size
from Q71IVcontrol import Diffie_Hellman,AES_CBC_MAC
from Crypto.Util.Padding import pad
from Q22 import xor

# %% Functions

class Client:

    def __init__(self,key,iv):
        print('Signature signing oracle is up: \n')
        self.Signing_Oracle = AES_CBC_MAC(key,iv)
        
    def prepare_message(self,from_id,tx_list):
        from_message = 'from=' + str(from_id)
        tx_list_message = '&tx_list=' 
        for item in tx_list:
            to_id = item[0]
            amount = item[1]
            tx_list_message += str(to_id) + ':' + str(amount) + ';'
        message = from_message + tx_list_message
        return message.encode()
    
    def send_message(self,from_id,tx_list):
        message = self.prepare_message(from_id,tx_list)
        mac = self.Signing_Oracle.get_mac(message)
        full_message = dict({'message': message, 'mac': mac})
        print('Sent message: ' + str(full_message) + '\n')
        return full_message

class Server:
    
    def __init__(self, key, iv):
        print('Signature verfication oracle is up: \n')
        self.Verification_Oracle = AES_CBC_MAC(key,iv)

    def receive_and_validate_message(self,full_message):
        print('Received message: ' + str(full_message) + '\n')
        message = full_message['message']; mac = full_message['mac']
        calcualted_signature = self.Verification_Oracle.get_mac(message)
        print('Received mac: ' + str(mac) + '\n')
        print('Calculated signature: ' + str(calcualted_signature) + '\n')
        if mac == calcualted_signature:
            print('Signature is valid!\n\n\n')
        else:
            print('Signature is invalid!!!!\n\n\n')

def length_extension_attack(full_message,client):
    fake_message = full_message.copy()
    id_extended = 1; tx_list_extended = [['a;1',1000],[2,10001]]
    print('The forged message should have specific structure that will allow us to pass the regex parser, therefore add padding at the start with a specific structure.\n')
    second_message = client.send_message(id_extended,tx_list_extended)
    m1 = full_message['message']; mac1 = full_message['mac']
    m2 = second_message['message']; mac2 = second_message['mac']
    p1 = m1[:block_size];               p1_ = m2[:block_size];
    p2 = m1[block_size:(2*block_size)]; p2_ = m2[block_size:(2*block_size)]
    p2_new = pad(p2,block_size);
    p3 = xor(mac1,p1_)
    p4 = p2_
    Q = p1 + p2_new + p3 + p4
    fake_message['message'] = Q
    fake_message['mac'] = mac2
    print('Forged message: ' + str(fake_message['message']))
    print('Forged message mac: ' + str(fake_message['mac']) + '\n')
    return fake_message
    

# %% Main

# Theres some big problem with this code i dont know where it is, should be somewhere with the implementation of AES-CBC-MAC

if __name__ == '__main__':
    print('\n\n\n')
    print('CBC-MAC message length extension attack simulation:\n')
    print('In this case we dont have IV control as it is predetermined to be a zero byte array.\n')
    key = Diffie_Hellman().run_key_exchange()
    iv = bytearray([0]*16)
    client = Client(key,iv)
    server = Server(key,iv)
    from_id = 0
    tx_list = [[5,1000],[3,10000]]
    print('\n')
    print('First we will look at an example which has a valid signature: \n')
    full_message = client.send_message(from_id,tx_list)
    server.receive_and_validate_message(full_message)
    print('Now we will look at a length extended attacked message which has a valid signature: \n')
    fake_message = length_extension_attack(full_message,client)
    server.receive_and_validate_message(fake_message)
    
    