# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:41:40 2021

@author: danie
"""

# https://cryptopals.com/sets/5/challenges/38

# %% Imports

import socket
from random import randint
from hashlib import sha256
from Q51 import modexp
from Q54Utils import HMAC_SHA256
from Q56Server import SERVER
from tqdm import tqdm

# %% Global variables

IP = '0.0.0.0'
PORT = 8820
BUFFER_SIZE = 4096

# %% Functions

class FakeSERVER:

    def __init__ (self):
        self.commands = ['SET_FIRST_CONTACT','SEND_PUBLIC_KEY','SEND_HMAC']
        self.N = None
        self.g = None
        self.k = None
        self.salt = None
        self.I = None
        self.v = None
        self.b = None
        self.B = None
        self.A = None
        self.u = None

    def receive_client_request(self,client_socket):
        """Receives the full message sent by the client
    
        Works with the protocol defined in the client's "send_request_to_server" function
    
        Returns:
            command: such as GET_CIPHER_SUIT, SEND_PUBLIC_KEY and etc
            params: the parameters of the command
    
        Example: 14SEND_PUBLIC_KEY p&g&A as input will result in sequenceNumber = 14 command = 'SEND_PUBLIC_KEY', params = 'p&g&A'
        """
        
        data = client_socket.recv(BUFFER_SIZE).decode();
        print('Received command from client: ' + data + '\n')
        if int(data[:4]) == len(data[4:]):
            try:
                data_split = data[4:].split(' ')
                command = data_split[0]; params = data_split[1]
                return command,params
            except:
                command = data[4:]; params = None
                return command,params
            
    def check_client_request(self,command, params):
        """Check if the params are good.
    
        For example, the filename to be copied actually exists
    
        Returns:
            valid: True/False
            error_msg: None if all is OK, otherwise some error message
        """
        if command in self.commands: 
            valid = True
            error_msg = ''
        else: 
            valid = False 
            error_msg = 'Please enter a valid command'
        return valid, error_msg
    
    
    def handle_client_request(self,command, params):
        """Create the response to the client, given the command is legal and params are OK
    
        Returns:
            response: the requested data
        """
        if command == 'SET_FIRST_CONTACT':
            blocks = params.split('&')
            self.N = int(blocks[0].split('=')[1])
            self.g = int(blocks[1].split('=')[1])
            self.k = int(blocks[2].split('=')[1])
            self.I = blocks[3].split('=')[1]
            P = blocks[4].split('=')[1]
            self.salt = randint(1,self.N**2)
            xH = sha256(str(self.salt).encode() + P.encode()).hexdigest()
            x = int(xH,16)
            self.v = modexp(self.g, x, self.N)
            del P, x, xH
            data = 'ACK'
        elif command == 'SEND_PUBLIC_KEY':
            blocks = params.split('&')
            if self.I == blocks[0].split('=')[1]:
                self.A = int(blocks[1].split('=')[1])
                self.b = randint(0,self.N)
                self.B = modexp(self.g,self.b,self.N)
                self.u = randint(0,2**128)
                data = 'salt=' + str(self.salt) + '&B=' + str(self.B) + '&u=' + str(self.u)
                print('Generated u: ' + str(self.u) + '\n')
            else:
                data = 'Stop hacking!'
        elif command == 'SEND_HMAC':
            print('\n \n \n \n')
            print('Brute force attack is running \n \n \n \n')
            for password in tqdm(range(2**12)): # dictionary
                P = str(password)
                x = int(sha256(str(self.salt).encode() + P.encode()).hexdigest(),16)
                v = modexp(self.g, x, self.N)
                S = modexp(self.A *modexp(v,self.u,self.N),self.b,self.N)
                K = sha256(str(S).encode()).digest()
                if params == HMAC_SHA256(K, str(self.salt).encode()):
                    print('Estimated secret: ' + str(P))
                    data = 'OK'
                    return data
            data = 'BAD' 
        return data
    
    def send_response_to_client(self,response, client_socket):
        """Create a protocol which sends the response to the client"""
        client_socket.send(response.encode())

    def receive_and_send_response(self,client_socket):
        command, params = self.receive_client_request(client_socket)
        valid, error_msg = self.check_client_request(command, params)
        if valid:
            response = self.handle_client_request(command, params)
            print('Sent response to client: ' + response + '\n')
            self.send_response_to_client(response, client_socket)
        else:
            self.send_response_to_client(error_msg, client_socket)

def main():
    # open socket with client
    print('\n')
    print('Bob \n')
    serverReal = SERVER()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print('Server is up and listening to connections\n')
    client_socket, address = server_socket.accept()
    print('Client connected\n')
    print('First time login parameters acknowledged\n')
    serverReal.receive_and_send_response(client_socket)
    client_socket.close()
    client_socket, address = server_socket.accept()
    print('User name: ' + str(serverReal.I) + ', salt: ' + str(serverReal.salt) + ', password verifier: ' + str(serverReal.v) + '.\n')
    print('\n \n \n')
    print('Fake server is up: \n')
    server = FakeSERVER()
    server.I = serverReal.I; server.salt = serverReal.salt;  server.v = serverReal.v; 
    server.N = serverReal.N; server.g = serverReal.g; server.k = serverReal.k;
    server.receive_and_send_response(client_socket)
    server.receive_and_send_response(client_socket)
    print('Close connection\n')
    client_socket.close()
    server_socket.close()

# %% Main

if __name__ == '__main__':
    main()