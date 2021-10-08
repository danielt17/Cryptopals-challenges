# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 16:56:25 2021

@author: danie
"""

# https://cryptopals.com/sets/5/challenges/36

# %% Imports

import socket
from random import randint
from Q51 import modexp
from hashlib import sha256
from Q54Utils import HMAC_SHA256

# %% Global variables

IP = '127.0.0.1'
PORT = 8820
BUFFER_SIZE = 4096

# %% Functions

class CLIENT:
    
    # Secure Remote Password (SRP) Protocol for TLS Authentication
    # https://datatracker.ietf.org/doc/html/rfc5054
    def __init__(self,I,P):
        self.N =    int('AC6BDB41 324A9A9B F166DE5E 1389582F AF72B665 1987EE07 FC319294\
                    3DB56050 A37329CB B4A099ED 8193E075 7767A13D D52312AB 4B03310D\
                    CD7F48A9 DA04FD50 E8083969 EDB767B0 CF609517 9A163AB3 661A05FB\
                    D5FAAAE8 2918A996 2F0B93B8 55F97993 EC975EEA A80D740A DBF4FF74\
                    7359D041 D5C33EA7 1D281E44 6B14773B CA97B43A 23FB8016 76BD207A\
                    436C6481 F1D2B907 8717461A 5B9D32E6 88F87748 544523B5 24B0D57D\
                    5EA77A27 75D2ECFA 032CFBDB F52FB378 61602790 04E57AE6 AF874E73\
                    03CE5329 9CCC041C 7BC308D8 2A5698F3 A8D0C382 71AE35F8 E9DBFBB6\
                    94B5C803 D89F7AE4 35DE236D 525F5475 9B65E372 FCD68EF2 0FA7111F\
                    9E4AFF73'.replace(' ','').lower(),16)
        self.g = 2
        self.k = 3
        self.I = I
        self.P = P
        self.commands = ['SET_FIRST_CONTACT','SEND_PUBLIC_KEY','SEND_HMAC']
        self.a = None
        self.A = None
        self.salt = None
        self.B = None
        
    def valid_request(self,request):
        """Check if the request is valid (is included in the available commands)
    
        Return:
            True if valid, False if not
        """
        if request in self.commands: valid = True
        else: valid = False 
        return valid
    
    def send_request_to_server(self,my_socket, request):
        """Send the request to the server. First the length of the request (2 digits), then the request itself
    
        Example: '14SEND_PUBLIC_KEY p&g&A'
        """
        data = '' + request
        if request == 'SET_FIRST_CONTACT':
            data = data + ' ' + 'N=' + str(self.N) + '&g=' + str(self.g) + '&k=' + str(self.k) + '&I=' + str(self.I) + '&P=' + str(self.P)
        elif request == 'SEND_PUBLIC_KEY':
            self.a = randint(1,self.N)
            self.A = modexp(self.g,self.a,self.N)
            data = data + ' ' + 'I=' + str(self.I) + '&A=' + str(self.A)
        elif request == 'SEND_HMAC':
            xH = sha256(str(self.salt).encode() + self.P.encode()).hexdigest()
            x = int(xH,16)
            S = modexp((self.B - self.k * modexp(self.g,x,self.N)),self.a + self.u * x,self.N)
            K = sha256(str(S).encode()).digest()
            data = data + ' ' + HMAC_SHA256(K,str(self.salt).encode())
            del x,xH,S,K
        if len(str(len(data))) < 4:
            data = '0'*(4-len(str(len(data)))) + str(len(data)) + data
        elif len(str(len(data))) == 4:
            data = str(len(data)) + data
        print('Sent command to server: ' + data + '\n')
        my_socket.send(data.encode())
        pass
    
    def handle_server_response(self,my_socket, request):
        """Receive the response from the server and handle it, according to the request"""
        if request in self.commands:
            gotData = my_socket.recv(BUFFER_SIZE).decode()
            print('Received command from server: ' + gotData + '\n')
            if request == 'SET_FIRST_CONTACT':
                data = gotData
            elif request == 'SEND_PUBLIC_KEY':
                blocks = gotData.split('&')
                self.salt = int(blocks[0].split('=')[1])
                self.B = int(blocks[1].split('=')[1])
                self.u = int(sha256(str(self.A).encode()+str(self.B).encode()).hexdigest(),16)
                data = 'Generated u: ' + str(self.u) + '\n'
            elif request == 'SEND_HMAC':
                data = gotData
        return data
    
    def send_and_recive(self,my_socket, request):
        if self.valid_request(request):
            self.send_request_to_server(my_socket, request)
            self.receivedData = self.handle_server_response(my_socket, request)
            if self.receivedData == 'CLOSE_CONNECTION':
                raise Exception('Unencrypted connection, closing connection')
        else:
            raise Exception('Send receive primitive is wrong')

def main():
    print('\n')
    print('Welcome to secure remote password (SRP) protocol simulation:\n')
    print('\n')
    print('Alice \n')
    print('Please enter your credentials below\n')
    I = input('Please enter your mail:\n')
    P = input('Please enter your password:\n')
    client = CLIENT(I,P)
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((IP, PORT))
    print('Setting up login parameters for the first time:\n')
    client.send_and_recive(my_socket, 'SET_FIRST_CONTACT')
    print('Sequential logins:\n')
    client.send_and_recive(my_socket, 'SEND_PUBLIC_KEY')
    print(client.receivedData)
    client.send_and_recive(my_socket, 'SEND_HMAC')
    if client.receivedData == 'OK':
        print('Succsefully entered the server')
    else:
        print('Failed to enter the server')
    my_socket.close()


# %% Main

if __name__ == '__main__':
    main()

