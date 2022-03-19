# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 17:27:59 2022

@author: danie
"""

# %% Imports

from Q71IVcontrol import Diffie_Hellman,AES_CBC_MAC

# %% Functions

class Client:

    def __init__(self,key,iv):
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
        print('parsing the message: ')
        message = full_message['message']; mac = full_message['mac']
        print('message: ' + str(message)); print('mac: ' + str(mac) + '\n')
        calcualted_signature = self.Verification_Oracle.get_mac(message)
        print('Calculated signature: ' + str(calcualted_signature) + '\n')
        if mac == calcualted_signature:
            print('Signature is valid!\n\n\n')
        else:
            print('Signature is invalid!!!!\n\n\n')
    
# %% Main

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
    full_message = client.send_message(from_id,tx_list)
    print('\n')
    print('First we will look at an example which has a valid signature: \n')
    server.receive_and_validate_message(full_message)
   
    