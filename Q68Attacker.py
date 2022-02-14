# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 12:54:34 2022

@author: danie
"""


# https://cryptopals.com/sets/6/challenges/48

# %% Imports

from Q67 import RSAPCKS1PaddingOracle
from Crypto.Util.number import long_to_bytes
import sys
from time import sleep
from pwn import hexdump
import socket

sys.setrecursionlimit(1500)

# %% Global variables

IP1 = '0.0.0.0'
IP2 = '127.0.0.1'
PORT1 = 8820
PORT2 = 8821
BUFFER_SIZE = 8192

# %% Functions

def print_with_hexdump(binary,send_or_receive):
    if send_or_receive == 'send_alice':
        print('Send command to client: \n')
    elif send_or_receive == 'receive_alice':
        print('Receive command from client: \n')
    if send_or_receive == 'send_bob':
        print('Send command to server: \n')
    elif send_or_receive == 'receive_bob':
        print('Receive command from server: \n')
    else:
        raise Exception('Bad send_or_receive fix your code!')
    print('------------------------------\n')
    print(hexdump(binary) + '\n')
    print('------------------------------\n')

class MITM:
    
    def __init__(self):
        self.allowed_cipher_suits = bytearray.fromhex("00 2f 00 35")
        self.message_type_client_hello = bytearray.fromhex("01")[0]
    
    def receive_alice_request(self, alice_socket):
        data = alice_socket.recv(BUFFER_SIZE)
        print_with_hexdump(data,'receive_alice')
        if data[5] == self.message_type_client_hello:
            request = 'Client_Hello'
        else:
            raise Exception('Request is invalid! fix your code!')
        return request, data
    
    def handle_alice_request(self, request, data):
        if request == 'Client_Hello':
            # 44 - 57
            print('Switching available cipher suits to include only the ones we can attack:\n')
            print('We can attack the following cipher suits: \n')
            print('00 2f - assigned value for TLS_RSA_WITH_AES_128_CBC_SHA\n')
            print('00 35 - assigned value for TLS_RSA_WITH_AES_256_CBC_SHA\n')
            data = data[:3] + bytearray.fromhex("00 2c 01 00 00 28") + data[9:44] + self.allowed_cipher_suits + data[58:]
        else:
            raise Exception('Request is invalid! fix your code!')
        return data
        
    
    def receive_bob_response(self, bob_socket):
        data = bob_socket.recv(BUFFER_SIZE)
        print_with_hexdump(data,'receive_bob')
        
    def handle_bob_response(self, request, data):
        return
    
    def send_to(self, response, cur_socket,socket_name):
        if socket_name == 'Alice':
            print_with_hexdump(response,'send_alice')
        elif socket_name == 'Bob':
            print_with_hexdump(response,'send_bob')
        else:
            raise Exception('Wrong socket name, fix it!')
        cur_socket.send(response)
    
    def receive_from_alice_send_to_bob_and_receive_send_back_to_alice(self,alice_socket, bob_socket):
        
    
def main():
    # open socket with client
    print('\n')
    print('Eve \n')
    ManInTheMiddle = MITM()
    eve_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    eve_socket.bind((IP1, PORT1))
    eve_socket.listen()
    print('Man in the middle is up and listening to connections\n')
    alice_socket, address = eve_socket.accept()
    print('Alice is connected\n')
    bob_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Connecting to Bob\n')
    bob_socket.connect((IP2, PORT2))
    print('Closing connection with Bob\n')
    bob_socket.close()
    print('Disconnecting Alice\n')
    alice_socket.close()
    print('Closing man in in the middle\n')
    eve_socket.close()

# %% Main

if __name__ == '__main__':
    main()