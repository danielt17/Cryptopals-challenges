# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 12:54:47 2022

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

IP = '0.0.0.0'
PORT = 8821
BUFFER_SIZE = 8192

# %% Functions

def print_with_hexdump(binary,send_or_receive,enb_pause=False):
    if send_or_receive == 'send':
        print('Send command to client: \n')
    elif send_or_receive == 'receive':
        print('Receive command from client: \n')
    else:
        raise Exception('Bad send_or_receive fix your code!')
    print('------------------------------\n')
    print(hexdump(binary) + '\n')
    print('------------------------------\n')
    if enb_pause:
        sleep(2)

class SERVER:

    def __init__ (self):
        self.available_cipher_suits = bytearray.fromhex("00 2f")
        self.message_type_client_hello = bytearray.fromhex("01")[0]

    def receive_client_request(self,client_socket):
        data = client_socket.recv(BUFFER_SIZE)
        print_with_hexdump(data,'receive',True)
        if data[5] == self.message_type_client_hello:
            request = 'Client_Hello'
        else:
            raise Exception('Request is invalid! fix your code!')
        return request, data
            
    def check_client_request(self, data):
        if (data[4] == len(data[5:])) & (data[8] == len(data[9:])):
            return True
        else:
            return False
    
    def handle_client_request(self, request, data):
        if request == 'Client_Hello':
            print('Received Client Hello.\n')
            if self.available_cipher_suits in data[44:-1]:
                handshake_record =          bytearray.fromhex("16") 
                protocol_version =          bytearray.fromhex("03 03")
                message_len =               bytearray.fromhex("00 31")
                record_header =             handshake_record + protocol_version + message_len
                handshake_message_type =    bytearray.fromhex("02")
                message_len_2 =             bytearray.fromhex("00 00 2d")
                handshake_header =          handshake_message_type + message_len_2
                server_version =            bytearray.fromhex("03 03")
                server_random =             long_to_bytes(getrandbits(32*8),32)
                session_id =                bytearray.fromhex("00")
                cipher_suites =             self.available_cipher_suits
                compression_methods =       bytearray.fromhex("00")
                # Server hello - packet
                data = record_header + handshake_header + server_version + server_random + session_id + cipher_suites + compression_methods
                print('Sending Server Hello.\n')
            else:
                raise Exception('No valid cipher suit, please fix your code!')
        else:
            raise Exception('Request is invalid! fix your code!')
        return data
    
    def send_response_to_client(self,client_socket,data):
        print_with_hexdump(data,'send',True)
        client_socket.send(data)

    def receive_and_send_response(self,client_socket):
        request, data = self.receive_client_request(client_socket)
        if self.check_client_request(data):
            data = self.handle_client_request(request, data)
            self.send_response_to_client(client_socket,data)
        else:
            raise Exception('Invalid request! request is not formatted correctly check your length')
    
        
def main():
    # open socket with client
    print('\n')
    print('Bob \n')
    server = SERVER()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print('Server is up and listening to connections\n')
    client_socket, address = server_socket.accept()
    server.receive_and_send_response(client_socket)
    print('Client connected\n')
    print('Close connection\n')
    client_socket.close()
    server_socket.close()

# %% Main

if __name__ == '__main__':
    main()



