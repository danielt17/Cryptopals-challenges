# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 12:54:34 2022

@author: danie
"""


# https://cryptopals.com/sets/6/challenges/48

# %% Imports

from Q51 import modexp
from Q67 import ceil,append_and_merge
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

def remove_pkcs(text):
    i = 2
    while text[i] != 0:
        i = i + 1
    return text[(i + 1):]

def print_with_hexdump(binary,send_or_receive,enb_pause=False):
    if send_or_receive == 'send_alice':
        print('Send command to client: \n')
    elif send_or_receive == 'receive_alice':
        print('Receive command from client: \n')
    elif send_or_receive == 'send_bob':
        print('Send command to server: \n')
    elif send_or_receive == 'receive_bob':
        print('Receive command from server: \n')
    else:
        raise Exception('Bad send_or_receive fix your code!')
    print('------------------------------\n')
    print(hexdump(binary) + '\n')
    print('------------------------------\n')
    if enb_pause:
        sleep(2)

class MITM:
    
    def __init__(self):
        self.allowed_cipher_suits = bytearray.fromhex("00 2f 00 35")
        self.message_type_client_hello = bytearray.fromhex("01")[0]
        self.message_type_server_hello = bytearray.fromhex("02")[0]
        self.message_type_server_certificate = bytearray.fromhex("0b")[0]
        self.message_type_server_key_exchange = bytearray.fromhex("0c")[0]
        self.message_type_server_hello_done = bytearray.fromhex("0e")[0]
        self.message_type_client_send_encrypted_key = bytearray.fromhex("10")[0]
        self.message_type_padding_validation = bytearray.fromhex("ff")[0]
        self.message_type_change_cipher_spec = bytearray.fromhex("14")[0]
        self.cipher_suit = None
        self.e = None
        self.n = None
        self.k = None
        self.cipherText = None
        self.dataBlock = None
        self.key = None
        self.change_client_cipher_suit_message = None
    
    def receive_alice_request(self, alice_socket):
        data = alice_socket.recv(BUFFER_SIZE)
        print_with_hexdump(data,'receive_alice',True)
        if data[0] == self.message_type_change_cipher_spec:
            request = 'Client_Change_Cipher_Spec'
        elif data[5] == self.message_type_client_hello:
            request = 'Client_Hello'
        elif data[5] == self.message_type_client_send_encrypted_key:
            request = 'Client_Send_Encrypted_Key'
        else:
            raise Exception('Request is invalid! fix your code!')
        return request, data
    
    def handle_alice_request(self, request, data):
        if request == 'Client_Hello':
            # 44 - 57
            print('Received Client Hello.\n')
            print('Switching available cipher suits to include only the ones we can attack:\n')
            print('We can attack the following cipher suits: \n')
            print('00 2f - assigned value for TLS_RSA_WITH_AES_128_CBC_SHA\n')
            print('00 35 - assigned value for TLS_RSA_WITH_AES_256_CBC_SHA\n')
            print('Removing all other cipher suits!\n')
            data = data[:3] + bytearray.fromhex("00 2c 01 00 00 28") + data[9:44] + self.allowed_cipher_suits + data[58:]
            print('Sending tempered Client Hello.\n')
        elif request == 'Client_Send_Encrypted_Key':
            print('Received Client Encrypted Key.\n')
            print('Encrypted secret key: ' + str(data[11:]) + ' \n')
            self.dataBlock = data[:11]
            self.cipherText = int.from_bytes(data[11:],'big')
            print('Recieved int cipher text: ' + str(self.cipherText) + '\n')
            data = data
        elif request == 'Client_Change_Cipher_Spec':
            print('Received client change spec message.\n')
            self.change_client_cipher_suit_message = data
            data = data
            print('Saving the message for later uses\n')
        else:
            raise Exception('Request is invalid! fix your code!')
        return data
        
    
    def receive_bob_response(self, bob_socket):
        data = bob_socket.recv(BUFFER_SIZE)
        if data[5] == self.message_type_server_hello:
            print_with_hexdump(data,'receive_bob',True)
            request = 'Server_Hello'
        elif data[5] == self.message_type_server_certificate:
            print_with_hexdump(data,'receive_bob',True)
            request = 'Server_Certificate'
        elif data[5] == self.message_type_server_key_exchange:
            print_with_hexdump(data,'receive_bob',True)
            request = 'Server_Key_Exchange'
        elif data[5] == self.message_type_server_hello_done:
            print_with_hexdump(data,'receive_bob',True)
            request = 'Server_Hello_Done'
        elif data[5] == self.message_type_padding_validation:
            print_with_hexdump(data,'receive_bob')
            request = 'Client_Send_Encrypted_Key'
        else:
            raise Exception('Request is invalid! fix your code!')
        return request,data
        
    def handle_bob_response(self, request, data):
        if request == 'Server_Hello':
            print('Received Server Hello.\n')
            self.cipher_suit = data[-3:-1]
            data = data
            print('Forwarding Server Hello.\n')
        elif request == 'Server_Certificate':
            print('Received Server Certificate.\n')
            data = data
            print('Forwarding Server Certificate.\n')
        elif request == 'Server_Key_Exchange':
            print('Received Server Key Exchange.\n')
            self.e = int.from_bytes(data[10:12],'big')
            self.k = int.from_bytes(data[12:14],'big')
            self.n = int.from_bytes(data[14:],'big')
            print('Public key: ' + str(self.e) + '\n')
            print('Modulos length in bytes: ' + str(self.k) + '\n')
            print('Public modulos: ' + str(self.n) + '\n')
            data = data
            print('Forwarding Server Key Exchange.\n')
        elif request == 'Server_Hello_Done':
            print('Received Server Hello Done.\n')
            data = data
            print('Forwarding Server Hello Done.\n')
        elif request == 'Client_Send_Encrypted_Key':
            data = data[10]
        else:
            raise Exception('Request is invalid! fix your code!')
        return data
    
    def send_to(self, response, cur_socket,socket_name):
        if socket_name == 'Alice':
            print_with_hexdump(response,'send_alice',True)
        elif socket_name == 'Bob':
            print_with_hexdump(response,'send_bob',True)
        else:
            raise Exception('Wrong socket name, fix it!')
        cur_socket.send(response)
    
    def receive_alice_send_bob(self,alice_socket,bob_socket):
        request, data = self.receive_alice_request(alice_socket)
        response = self.handle_alice_request(request, data)
        self.send_to(response, bob_socket, 'Bob')
        
    def receive_bob_send_alice(self,alice_socket,bob_socket):
        request, data = self.receive_bob_response(bob_socket)
        response = self.handle_bob_response(request, data)
        self.send_to(response, alice_socket, 'Alice')
    
    def receive_from_alice_send_to_bob_and_receive_send_back_to_alice(self,alice_socket, bob_socket):
        self.receive_alice_send_bob(alice_socket,bob_socket)
        self.receive_bob_send_alice(alice_socket,bob_socket)
    
    def prepare_data_for_attack(self,alice_socket,bob_socket):
        request, data = self.receive_alice_request(alice_socket)
        self.handle_alice_request(request, data)
        request, data = self.receive_alice_request(alice_socket)
        self.handle_alice_request(request, data)
    
    def prepare_fake_data_block(self,c_cur):
        data = self.dataBlock + long_to_bytes(c_cur,self.k)
        return data
    
    def padding_oracle(self,c_cur,bob_socket):
        data = self.prepare_fake_data_block(c_cur)
        print_with_hexdump(data,'send_bob')
        bob_socket.send(data)
        request,data = self.receive_bob_response(bob_socket)
        data = self.handle_bob_response(request, data)
        if data == 1:
            return True
        else:
            return False
    
    def post_attack_message(self,bob_socket):
        self.send_to(self.dataBlock + long_to_bytes(self.cipherText,self.k),bob_socket,'Bob')
        request, data = self.receive_bob_response(bob_socket)
        self.handle_bob_response(request, data)
    
    def Bleichenbacher_98_attack(self,bob_socket):
        print("Starting Bleichenbacher's PKCS 1.5 attack: \n")
        sleep(5)
        e = self.e; n = self.n;
        B = 2 ** (8 * (self.k - 2))
        # Step 1: Blinding. (we don't actually need it cause c is known to be PKCS conforming)
        c = self.cipherText
        print('Step 1: Blinding.\n')
        print('Intializing c (the cipher text is already PKCS conforming): ' + str(c) + '\n')
        M = [(2 * B, 3 * B - 1)] # This is the range between \x00\x02\x00...\x00  to \x00\x02\xff...\xff
        print('Intializing M limits [2*B, 3*B-1]: ' + str(M) + '\n')
        i = 1;
        Calls_to_oracle = 0;
        print('Intializing i: ' + str(i) + '\n')
        print("Starting Bleichenbacher's attack iterative loop:\n")
        while True:
            print('Iteration number: ' + str(i) + '\n')
            print('--------------------------------------\n')
            # Step 2: Searching for PKCS conforming messages
            print('Step 2: Searching for PKCS conforming messages.\n')
            if i == 1:
                print('Step 2.a: Starting the search.\n')
                s = ceil(n,3*B)
                while not self.padding_oracle((c * modexp(s, e, n)) % n,bob_socket):
                    s = s + 1
                    Calls_to_oracle += 1
                    if Calls_to_oracle % 100 == 0:
                        print('Calls to Oracle: ' + str(Calls_to_oracle))
            elif len(M) >= 2:
                print('Step 2.b: Searching with more than one interval left.\n')
                s = s + 1
                while not self.padding_oracle((c * modexp(s, e, n)) % n,bob_socket):
                    s = s + 1
                    Calls_to_oracle += 1
                    if Calls_to_oracle % 100 == 0:
                        print('Calls to Oracle: ' + str(Calls_to_oracle))
            elif i > 1 and len(M) == 1:
                print('Step 2.c: Searching with one interval left.\n')
                a = M[0][0]; b = M[0][1];
                if a == b: break
                r = ceil(2*(b * s - 2 * B),n)
                s = ceil(2 * B + r * n,b)
                while not self.padding_oracle((c * modexp(s, e, n)) % n,bob_socket):
                    s = s + 1
                    if s > (3 * B + r * n)//a:
                        r = r + 1
                        s = ceil(2 * B + r * n,b) 
                    Calls_to_oracle += 1
                    if Calls_to_oracle % 100 == 0:
                        print('Calls to Oracle: ' + str(Calls_to_oracle))
            # Step 3: arrowing the set of solutions
            print('Step 3: Narrowing the set of solutions.\n')
            Ms = []
            for j in range(len(M)):
                a = M[j][0]; b = M[j][1]
                r_lower = ceil(a * s - (3 * B) + 1,n)
                r_upper = (b * s - (2 * B))//n
                for r in range(r_lower,r_upper + 1):
                    lower = max(a,ceil(2 * B + r * n,s))
                    upper = min(b,(3 * B - 1  + r * n)//s)
                    append_and_merge(Ms, lower, upper)
            if len(Ms) == 0:
                raise Exception('Unexpected error: there are 0 intervals.')
            M = Ms
            i = i + 1
            print('Lower limit: \n')
            print('--------------------------\n')
            print(hexdump(long_to_bytes(M[0][0],self.k)) + '\n')
            print('\n')
            print('--------------------------\n')
            print('\n')
        # Step 4: Computing the solution
        print('Step 4: Computing the solution.\n')
        m = M[0][0] % n
        print('Solution: ' + str(m) + '\n')
        self.key = remove_pkcs(long_to_bytes(m,self.k))
        print('Recovered secret key: ' + str(self.key) + '\n')
        self.post_attack_message(bob_socket)
        
    def send_client_change_cipher_spec(self,bob_socket):
        self.send_to(self.change_client_cipher_suit_message, bob_socket,'Bob')
    
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
    ManInTheMiddle.receive_from_alice_send_to_bob_and_receive_send_back_to_alice(alice_socket,bob_socket)
    ManInTheMiddle.receive_bob_send_alice(alice_socket,bob_socket)
    ManInTheMiddle.receive_bob_send_alice(alice_socket,bob_socket)
    ManInTheMiddle.receive_bob_send_alice(alice_socket,bob_socket)
    ManInTheMiddle.prepare_data_for_attack(alice_socket,bob_socket)
    ManInTheMiddle.Bleichenbacher_98_attack(bob_socket)
    ManInTheMiddle.send_client_change_cipher_spec(bob_socket)
    print('Closing connection with Bob\n')
    bob_socket.close()
    print('Disconnecting Alice\n')
    alice_socket.close()
    print('Closing man in in the middle\n')
    eve_socket.close()

# %% Main

if __name__ == '__main__':
    main()
