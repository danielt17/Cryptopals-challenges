# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 12:08:16 2021

@author: danie
"""


# https://cryptopals.com/sets/5/challenges/34

# %% Imports

from Q44 import SHA1
from Crypto.Util.number import long_to_bytes
from Q51 import DiffieHellman
from Crypto.Random import get_random_bytes
import socket
from binascii import unhexlify
from Q28 import aes_cbc_encrypt,aes_cbc_decrypt

# %% Global variables

IP = '0.0.0.0'
PORT = 8820
BUFFER_SIZE = 1024

# %% Functions

class SERVER:

    def __init__ (self):
        self.p = None
        self.g = None
        self.A = None
        self.B = None
        self.deffieHellman = None
        self.s = None
        self.cipherSuits = 'DH_AES_CBC&RSA_AES_CBC'
        self.agreedCipherSuit = None
        self.iv = get_random_bytes(16)
        self.key = None
        self.sendMessage = None
        self.recievedMessage = None

    def receive_client_request(self,client_socket):
        """Receives the full message sent by the client
    
        Works with the protocol defined in the client's "send_request_to_server" function
    
        Returns:
            command: such as GET_CIPHER_SUIT, SEND_PUBLIC_KEY and etc
            params: the parameters of the command
    
        Example: 14SEND_PUBLIC_KEY p&g&A as input will result in sequenceNumber = 14 command = 'SEND_PUBLIC_KEY', params = 'p&g&A'
        """
        
        data = client_socket.recv(BUFFER_SIZE).decode();
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
        commands = ['GET_CIPHER_SUIT','AGREED_CIPHER_SUIT','SEND_PUBLIC_KEY','SEND_ENCRYPTED','EXIT']
        if command in commands: 
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
        if command == 'GET_CIPHER_SUIT':
            data = self.cipherSuits
        elif command == 'AGREED_CIPHER_SUIT':
            if params in self.cipherSuits:
                self.agreedCipherSuit = params
                data = 'Agreed on ' + params
        elif command == 'SEND_PUBLIC_KEY':
            blocks = params.split('&')
            self.p = int(blocks[0].split('=')[1])
            self.g = int(blocks[1].split('=')[1])
            self.B = int(blocks[2].split('=')[1])
            self.deffieHellman = DiffieHellman(self.p,self.g)
            self.A = self.deffieHellman.public_key()
            self.s = self.deffieHellman.shared_secret(self.B)
            self.key = unhexlify(SHA1(long_to_bytes(self.s)))[:16]
            data = str(self.A)
        elif command == 'SEND_ENCRYPTED':
            blocks = params.split('&')
            cipherText = unhexlify(blocks[0][len('cipherText='):])
            ivRecived = unhexlify(blocks[1][len('iv='):])
            self.recievedMessage = aes_cbc_decrypt(cipherText,self.key,ivRecived).decode()
            self.sendMessage = self.recievedMessage.encode()
            data = aes_cbc_encrypt(self.sendMessage,self.key,self.iv).hex() + '&' + self.iv.hex()
        elif command == 'EXIT':
            data = 'Stopping the connection'
        return data
    
    
    def send_response_to_client(self,response, client_socket):
        """Create a protocol which sends the response to the client"""
        client_socket.send(response.encode())

    def receive_and_send_response(self,client_socket):
        command, params = self.receive_client_request(client_socket)
        valid, error_msg = self.check_client_request(command, params)
        if valid:
            response = self.handle_client_request(command, params)
            self.send_response_to_client(response, client_socket)
        else:
            self.send_response_to_client(error_msg, client_socket)

def main():
    # open socket with client
    print('\n')
    server = SERVER()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print('Server is up and listening to connections\n')
    client_socket, address = server_socket.accept()
    print('Client connected\n')
    print('Sending possible cipher suits: DH_AES_CBC & RSA_AES_CBC\n')
    server.receive_and_send_response(client_socket)
    server.receive_and_send_response(client_socket)
    print('Agreed cipher suit: ' + server.agreedCipherSuit + '\n')
    print('Recieving Deffie Hellman paramters, and user public key, while sending the server public key, and creating a shared secret:\n')
    server.receive_and_send_response(client_socket)
    print('Generated shared secret: ' + str(server.s) + '\n')
    server.receive_and_send_response(client_socket)
    print('Received message after decryption: ' + server.recievedMessage +  '\n')
    print('Sending the message back\n')
    print('Close connection\n')
    client_socket.close()
    server_socket.close()

# %% Main

if __name__ == '__main__':
    main()
