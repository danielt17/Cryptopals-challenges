# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:02:55 2021

@author: danie
"""

# https://cryptopals.com/sets/5/challenges/35

# %% Imports

from Q44 import SHA1
from Crypto.Util.number import long_to_bytes
from Q51 import DiffieHellman
import socket
from binascii import unhexlify
from Q28 import aes_cbc_decrypt

# %% Global variables

IP1 = '0.0.0.0'
IP2 = '127.0.0.1'
PORT1 = 8820
PORT2 = 8821
BUFFER_SIZE = 1024

# %% Functions

class MITM:
    
    def __init__(self):
        self.p = None
        self.g = None
        self.Aoriginal = None
        self.Acrafted = None
        self.Boriginal = None
        self.Bcrafted = None
        self.deffieHellman = None
        self.s = None
        self.cipherSuit = 'DH_AES_CBC'
        self.agreedCipherSuit = None
        self.ivAlice = None
        self.ivBob = None
        self.key = None
        self.request = None
        self.sendMessage = None
        self.recievedMessage = None
    
    def receive_alice_request(self, alice_socket):
        """Receives the full message sent by the alice
    
        Works with the protocol defined in the client's "send_request_to_server" function
    
        Returns:
            command: such as GET_CIPHER_SUIT, SEND_PUBLIC_KEY and etc
            params: the parameters of the command
    
        Example: 14SEND_PUBLIC_KEY p&g&A as input will result in sequenceNumber = 14 command = 'SEND_PUBLIC_KEY', params = 'p&g&A'
        """
        
        data = alice_socket.recv(BUFFER_SIZE).decode();
        if int(data[:4]) == len(data[4:]):
            try:
                data_split = data[4:].split(' ')
                command = data_split[0]; params = data_split[1]
                return command,params
            except:
                command = data[4:]; params = None
                return command,params
    
    def handle_alice_request_and_send_to_bob(self, command, params):
        """Create the response to the client, given the command is legal and params are OK
    
        Returns:
            response: the requested data
        """
        self.request = command
        if command == 'GET_CIPHER_SUIT':
            data = 'GET_CIPHER_SUIT'
        elif command == 'AGREED_CIPHER_SUIT':
            self.agreedCipherSuit = params
            if self.agreedCipherSuit != self.cipherSuit:
                raise Exception('Cant preform man in the middle, no matching cipher suit')
            data = self.request + ' ' + params
        elif command == 'SEND_PUBLIC_INFO':
            blocks = params.split('&')
            self.p = int(blocks[0].split('=')[1])
            self.g = int(blocks[1].split('=')[1])
            data = 'SEND_PUBLIC_INFO' + ' ' + 'p=' + str(self.p) + '&' + 'g=' + str(self.g)
        elif command == 'SEND_PUBLIC_KEY':
            self.Aoriginal = int(params.split('=')[1])
            self.deffieHellman = DiffieHellman(self.p,self.g)
            if self.g == 1:
                self.s = [1] # for g = 1 one expects s = 1 because of g^a mod p = 1 = A therefore, s = A^b mod p = 1^b mod p = 1
            elif self.g == self.p:
                self.s = [0] 
            elif self.g == (self.p - 1): # s = (p-1)^ab mod p = (-1)^ab mod p
                self.s = [1,-1]
            self.key = []
            for sCur in self.s:
                self.key.append(unhexlify(SHA1(long_to_bytes(sCur)))[:16])
            data = 'SEND_PUBLIC_KEY' ' '+ 'A=' + str(self.Aoriginal)
        elif command == 'SEND_ENCRYPTED':
            blocks = params.split('&')
            cipherText = unhexlify(blocks[0][len('cipherText='):])
            self.ivAlice = unhexlify(blocks[1][len('iv='):])
            for key in self.key:
                try:
                    self.sendMessage = aes_cbc_decrypt(cipherText,key,self.ivAlice).decode()
                    self.key = key
                except:
                    print(str(key) + ' is not the correct key \n')
            print('Decrypted text from Alice: ' + self.sendMessage + '\n')
            data = command + ' ' + params
        elif command == 'EXIT':
            data = 'Stopping the connection'
        if len(str(len(data))) < 4:
            data = '0'*(4-len(str(len(data)))) + str(len(data)) + data
        elif len(str(len(data))) == 4:
            data = str(len(data)) + data
        return data
    
    def handle_bob_response_and_send_to_alice(self,bob_socket):
        gotData = bob_socket.recv(BUFFER_SIZE).decode()
        if self.request == 'GET_CIPHER_SUIT':
            availableSuits = gotData.split('&')
            if self.cipherSuit in availableSuits:
                data = self.cipherSuit
            else:
                raise Exception('Cant preform man in the middle no valid cipher suit is available')
        elif self.request == 'AGREED_CIPHER_SUIT':
            data = gotData
        elif self.request == 'SEND_PUBLIC_INFO':
            data = gotData
        elif self.request == 'SEND_PUBLIC_KEY':
            self.Boriginal = int(gotData)
            data = str(self.Boriginal)
        elif self.request == 'SEND_ENCRYPTED':
            blocks = gotData.split('&')
            cipherText = unhexlify(blocks[0]); self.ivBob = unhexlify(blocks[1])
            self.recivedMessage = aes_cbc_decrypt(cipherText,self.key,self.ivBob).decode()
            print('Decrypted text from Bob: ' + self.recivedMessage + '\n')
            data = gotData
        return data
    
    def send_to(self, response, cur_socket):
        """Create a protocol which sends the response to the client"""
        cur_socket.send(response.encode())
    
    def receive_from_alice_send_to_bob_and_receive_send_back_to_alice(self,alice_socket, bob_socket):
        command, params = self.receive_alice_request(alice_socket)
        request = self.handle_alice_request_and_send_to_bob(command, params)
        print('Sent request to Bob: ' + request + '\n')
        self.send_to(request, bob_socket)
        self.receivedData = self.handle_bob_response_and_send_to_alice(bob_socket)
        print('Sent request to Alice: ' + self.receivedData + '\n')
        self.send_to(self.receivedData, alice_socket)
    
def main():
    # open socket with client
    print('\n')
    print('Eve \n')
    for i in range(3):
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
        print('Receiving cipher suit request from alice, getting anwser from bob, forcing our choice of cipher suit: ' + ManInTheMiddle.cipherSuit + '\n')
        ManInTheMiddle.receive_from_alice_send_to_bob_and_receive_send_back_to_alice(alice_socket, bob_socket)
        print('Agreed cipher suit communication \n')
        ManInTheMiddle.receive_from_alice_send_to_bob_and_receive_send_back_to_alice(alice_socket, bob_socket)
        print('Man in the middle with respect to A,B parameters of Deffie-Hellman key exchange')
        ManInTheMiddle.receive_from_alice_send_to_bob_and_receive_send_back_to_alice(alice_socket, bob_socket)
        ManInTheMiddle.receive_from_alice_send_to_bob_and_receive_send_back_to_alice(alice_socket, bob_socket)
        print('Generated shared secret: ' + str(ManInTheMiddle.s) + '\n')
        print('Decrypting communication between Alice and Bob \n')
        ManInTheMiddle.receive_from_alice_send_to_bob_and_receive_send_back_to_alice(alice_socket, bob_socket)
        print('Closing connection with Bob\n')
        bob_socket.close()
        print('Disconnecting Alice\n')
        alice_socket.close()
        print('Closing man in in the middle\n')
        eve_socket.close()
        print('\n \n \n \n \n \n')

# %% Main

if __name__ == '__main__':
    main()