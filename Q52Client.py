# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 12:55:24 2021

@author: danie
"""

# https://cryptopals.com/sets/5/challenges/34

# %% Imports

import socket
from Crypto.Util.number import long_to_bytes
from Q51 import DiffieHellman
from Crypto.Random import get_random_bytes
from Q44 import SHA1
from binascii import unhexlify
from Q28 import aes_cbc_encrypt,aes_cbc_decrypt

# %% Global variables

IP = '127.0.0.1'
PORT = 8820

BUFFER_SIZE = 1024

# %% Functions

class CLIENT:
    
    def __init__(self):
        self.p = int('ffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff',16)
        self.g = 2
        self.deffieHellman = DiffieHellman(self.p,self.g)
        self.A = self.deffieHellman.public_key()
        self.B = None
        self.s = None
        self.receivedData = None
        self.cipherSuit = 'DH_AES_CBC'
        self.iv = get_random_bytes(16)
        self.key = None
        self.sendMessage = None
        self.recivedMessage = None
        
    def valid_request(self,request):
        """Check if the request is valid (is included in the available commands)
    
        Return:
            True if valid, False if not
        """
        commands = ['GET_CIPHER_SUIT','AGREED_CIPHER_SUIT','SEND_PUBLIC_KEY','SEND_ENCRYPTED','EXIT']
        if request in commands: valid = True
        else: valid = False 
        return valid
    
    def send_request_to_server(self,my_socket, request):
        """Send the request to the server. First the length of the request (2 digits), then the request itself
    
        Example: '14SEND_PUBLIC_KEY p&g&A'
        """
        data = '' + request
        if request == 'GET_CIPHER_SUIT':
            pass
        elif request == 'AGREED_CIPHER_SUIT':
            data = data + ' ' + self.receivedData
        elif request == 'SEND_PUBLIC_KEY':
            data = data + ' ' + 'p=' + str(self.p) + '&' + 'g=' + str(self.g) + '&' + 'A=' + str(self.A)
        elif request == 'SEND_ENCRYPTED':
            cipherText = aes_cbc_encrypt(self.sendMessage,self.key,self.iv).hex()
            data = data + ' ' + 'cipherText=' + cipherText + '&iv=' + self.iv.hex() # covert back to str
        if len(str(len(data))) < 4:
            data = '0'*(4-len(str(len(data)))) + str(len(data)) + data
        elif len(str(len(data))) == 4:
            data = str(len(data)) + data
        my_socket.send(data.encode())
        pass
    
    def handle_server_response(self,my_socket, request):
        """Receive the response from the server and handle it, according to the request"""
        if request == 'GET_CIPHER_SUIT' or request == 'AGREED_CIPHER_SUIT' or request == 'SEND_PUBLIC_KEY' or 'SEND_ENCRYPTED':
            gotData = my_socket.recv(BUFFER_SIZE).decode()
            if request == 'GET_CIPHER_SUIT':
                availableSuits = gotData.split('&')
                if self.cipherSuit in availableSuits:
                    data = self.cipherSuit
                else:
                    data = 'CLOSE_CONNECTION'
            elif request == 'AGREED_CIPHER_SUIT':
                data = gotData
            elif request == 'SEND_PUBLIC_KEY':
                self.B = int(gotData)
                self.s = self.deffieHellman.shared_secret(self.B)
                self.key = unhexlify(SHA1(long_to_bytes(self.s)))[:16]
                data = None
            elif request == 'SEND_ENCRYPTED':
                blocks = gotData.split('&')
                cipherText = unhexlify(blocks[0]); ivRecived = unhexlify(blocks[1])
                self.recivedMessage = aes_cbc_decrypt(cipherText,self.key,ivRecived).decode()
                data = self.recivedMessage
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
    # open socket with the server.
    print('\n')
    client = CLIENT()
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((IP, PORT))
    print('Welcome to Deffie-Hellman key exchange simulation:\n')
    print('Request possible cipher suits:\n')
    client.send_and_recive(my_socket, 'GET_CIPHER_SUIT')
    print('Send agreed possible cipher suit: ' + client.receivedData + '\n')
    client.send_and_recive(my_socket, 'AGREED_CIPHER_SUIT')
    print('Sever response: ' + client.receivedData  + '\n')
    print('Send p, g, A\n')
    client.send_and_recive(my_socket, 'SEND_PUBLIC_KEY')
    print('Receive B\n')
    print('Generated shared secret: ' + str(client.s) + '\n')
    client.sendMessage = b'Hello-There!'
    print('Sending message: ' + str(client.sendMessage) + '\n')
    print('Send AES-CBC(SHA1(s)[0:16], iv=random(16), msg) + iv\n')
    client.send_and_recive(my_socket, 'SEND_ENCRYPTED')
    print('Receive AES-CBC(SHA1(s)[0:16], iv=random(16), As msg) + iv\n' )
    print('Received message: ' + client.recivedMessage + '\n')
    print('Close connection\n') 
    my_socket.close()

if __name__ == '__main__':
    main()