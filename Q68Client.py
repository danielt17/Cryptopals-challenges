# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 12:41:17 2022

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
from random import getrandbits

sys.setrecursionlimit(1500)

# %% Global variables

IP = '127.0.0.1'
PORT = 8820
BUFFER_SIZE = 8192

# %% Functions

def print_with_hexdump(binary,send_or_receive,enb_pause=False):
    if send_or_receive == 'send':
        print('Send command to server: \n')
    elif send_or_receive == 'receive':
        print('Receive command from server: \n')
    else:
        raise Exception('Bad send_or_receive fix your code!')
    print('------------------------------\n')
    print(hexdump(binary) + '\n')
    print('------------------------------\n')
    if enb_pause:
        sleep(2)

class CLIENT:
    
    def __init__(self):
        self.valid_requests = ['Client_Hello']
        self.cipher_suit = None
        self.message_type_server_hello = bytearray.fromhex("02")[0]
        
    def valid_request(self,request):
        return request in self.valid_requests
        
    def send_request_to_server(self,my_socket, request):
        print('\n')
        if request == 'Client_Hello':
            print('Initiate Client Hello: \n')
            # Basic client hello without extension fields, length will be different because we dont use the extensions
            handshake_record =          bytearray.fromhex("16") 
            protocol_version =          bytearray.fromhex("03 03")
            message_len =               bytearray.fromhex("00 36") # message length in bytes to follow
            record_header =             handshake_record + protocol_version + message_len
            handshake_message_type =    bytearray.fromhex("01")
            message_len_2 =             bytearray.fromhex("00 00 32") # yeah TLS is a really stupidly built 
            handshake_header =          handshake_message_type + message_len_2
            client_version =            bytearray.fromhex("03 03")
            client_random =             long_to_bytes(getrandbits(32*8),32)
            session_id =                bytearray.fromhex("00")
            cipher_suites =             bytearray.fromhex("00 20 cc a8 c0 2f 00 9c 00 2f c0 12 00 0a")
            compression_methods =       bytearray.fromhex("00")
            # Client hello - packet
            data = record_header + handshake_header + client_version + client_random + session_id + cipher_suites + compression_methods
        print_with_hexdump(data,'send',True)
        my_socket.send(data)
        
    def receive_server_response(self,my_socket):
        data = my_socket.recv(BUFFER_SIZE)
        print_with_hexdump(data,'receive',True)
        if data[5] == self.message_type_server_hello:
            request = 'Server_Hello'
        else:
            raise Exception('Request is invalid! fix your code!')
        return request, data
    
    def handle_server_response(self,request, data):
        if request == 'Server_Hello':
            print('Received Server Hello.\n')
            self.cipher_suit = data[-3:-1]
            data = 'wait'
        return data
    
    def send_and_recive(self,my_socket, request):
        if self.valid_request(request):
            self.send_request_to_server(my_socket, request)
            request, data = self.receive_server_response(my_socket)
            data = self.handle_server_response(request, data)
            return data
        else:
            raise Exception('Invalid command! fix your code!')
        

def main():
    # open socket with the server.
    print('\n')
    print('Alice \n')
    client = CLIENT()
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((IP, PORT))
    data = client.send_and_recive(my_socket, 'Client_Hello')
    print('Close connection\n') 
    my_socket.close()


# %% Main

if __name__ == '__main__':
    main()