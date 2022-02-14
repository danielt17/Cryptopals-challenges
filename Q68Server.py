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

sys.setrecursionlimit(1500)

# %% Global variables

IP = '0.0.0.0'
PORT = 8821
BUFFER_SIZE = 8192

# %% Functions

class SERVER:

    def __init__ (self):
        

    def receive_client_request(self,client_socket):
        
            
    def check_client_request(self,command, params):
    
    
    def handle_client_request(self,command, params):
    
    
    def send_response_to_client(self,response, client_socket):
        

    def receive_and_send_response(self,client_socket):
        
        

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
    print('Client connected\n')
    print('Close connection\n')
    client_socket.close()
    server_socket.close()

# %% Main

if __name__ == '__main__':
    main()



