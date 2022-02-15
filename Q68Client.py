# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 12:41:17 2022

@author: danie
"""


# https://cryptopals.com/sets/6/challenges/48

# %% Imports

from Q51 import modexp
from Crypto.Util.number import long_to_bytes
import sys
from time import sleep
from pwn import hexdump
import socket
from random import getrandbits
from Crypto.Random import get_random_bytes
from Crypto.Cipher.AES import block_size
from Q28 import aes_cbc_encrypt, aes_cbc_decrypt
from hashlib import sha1

sys.setrecursionlimit(1500)

# %% Global variables

IP = '127.0.0.1'
PORT = 8820
BUFFER_SIZE = 8192

# %% Functions

class AESCBC:
    
    def __init__(self,key,iv):
        self.key = key
        self.iv = iv

    def encrypt(self,plainText):
        return aes_cbc_encrypt(plainText.encode(),self.key,self.iv)
    
    def decrypt(self,cipherText):
        return aes_cbc_decrypt(cipherText,self.key,self.iv)
    
def SHA1_MAC(key,plainText):
    return sha1(key + plainText.encode()).digest()
    
def PKCS1_pad(plainTextBytes,k):
    # Implemented according to RFC 3447 
    # https://datatracker.ietf.org/doc/html/rfc3447#page-23
    PS = b''
    for _ in range(k - len(plainTextBytes) - 3): 
        PS_current = 0
        while PS_current == 0:
            PS_current = getrandbits(8)
        PS = PS +  long_to_bytes(PS_current)
    return b'\x00\x02' + PS + b'\x00' + plainTextBytes
    
def encrypt(plainText,e,n,k):
    # plainText input as bytes object
    plainTextPadded = int.from_bytes(PKCS1_pad(plainText,k),'big')
    print('Padded plain text int: ' + str(plainTextPadded) + '\n')
    return modexp(plainTextPadded, e, n)

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
        self.message_type_server_hello = bytearray.fromhex("02")[0]
        self.message_type_server_certificate = bytearray.fromhex("0b")[0]
        self.message_type_server_key_exchange = bytearray.fromhex("0c")[0]
        self.message_type_server_hello_done = bytearray.fromhex("0e")[0]
        self.cipher_suit = None
        self.e = None
        self.n = None
        self.k = None
        self.key = None
        self.encryption_iv = None
        self.symmetric_cipher = None
        
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
        elif request == 'Client_Send_Encrypted_Key':
            print('Send secret AES-128 key.\n')
            handshake_record =          bytearray.fromhex("16") 
            protocol_version =          bytearray.fromhex("03 03")
            message_len =               bytearray.fromhex("01 06") # message length in bytes to follow
            record_header =             handshake_record + protocol_version + message_len
            handshake_message_type =    bytearray.fromhex("10")
            message_len_2 =             bytearray.fromhex("00 01 02") # yeah TLS is a really stupidly built 
            handshake_header =          handshake_message_type + message_len_2
            self.key =                  get_random_bytes(block_size) # AES-128 key
            print('Secret key: ' + str(self.key) + ' \n')
            cipherText_len =            bytearray.fromhex("01 00")
            cipherText_int =            encrypt(self.key,self.e,self.n,self.k)
            print('Encrypted secret key int: ' + str(cipherText_int) + ' \n')
            cipherText = long_to_bytes(cipherText_int,self.k)
            data = record_header + handshake_header + cipherText_len + cipherText
        elif request == 'Client_Change_Cipher_Spec':
            print('Changing client cipher spec.\n')
            change_cipher_spec =        bytearray.fromhex("14") 
            protocol_version =          bytearray.fromhex("03 03")
            message_len =               bytearray.fromhex("00 01") 
            payload =                   bytearray.fromhex("01")
            data = change_cipher_spec + protocol_version + message_len + payload
        elif request == 'Client_Handshake_Finished':
            handshake_record =          bytearray.fromhex("16") 
            protocol_version =          bytearray.fromhex("03 03")
            message_len =               bytearray.fromhex("00 46") # message length in bytes to follow
            record_header =             handshake_record + protocol_version + message_len
            self.iv =                   get_random_bytes(block_size)
            self.symmetric_cipher =     AESCBC(self.key,self.iv)
            super_secret_message =      'Super Secret Message!!!!!!'
            encrypted_data =            self.symmetric_cipher.encrypt(super_secret_message) # 32 bytes
            mac_len =                   bytearray.fromhex("00 20")
            mac =                       SHA1_MAC(self.key,super_secret_message) # 20 bytes
            data = record_header + self.iv + encrypted_data + mac_len + mac
        else:
            raise Exception('Wrong request, fix your code!')
        print_with_hexdump(data,'send',True)
        my_socket.send(data)
        
    def receive_server_response(self,my_socket):
        data = my_socket.recv(BUFFER_SIZE)
        print_with_hexdump(data,'receive',True)
        if data[5] == self.message_type_server_hello:
            request = 'Server_Hello'
        elif data[5] == self.message_type_server_certificate:
            request = 'Server_Certificate' 
        elif data[5] == self.message_type_server_key_exchange:
            request = 'Server_Key_Exchange'
        elif data[5] == self.message_type_server_hello_done:
            request = 'Server_Hello_Done'
        else:
            raise Exception('Request is invalid! fix your code!')
        return request, data
    
    def handle_server_response(self,request, data):
        if request == 'Server_Hello':
            print('Received Server Hello.\n')
            self.cipher_suit = data[-3:-1]
        elif request == 'Server_Certificate':
            print('Received Server Certificate.\n')
        elif request == 'Server_Key_Exchange':
            print('Received Server Key Exchange.\n')
            self.e = int.from_bytes(data[10:12],'big')
            self.k = int.from_bytes(data[12:14],'big')
            self.n = int.from_bytes(data[14:],'big')
            print('Public key: ' + str(self.e) + '\n')
            print('Modulos length in bits: ' + str(self.k * 8) + '\n')
            print('Public modulos: ' + str(self.n) + '\n')
        elif request == 'Server_Hello_Done':
            print('Received Server Hello Done.\n')
        else:
            raise Exception('Request is invalid! fix your code!')
    
    def process_server_response(self,my_socket):
        request, data = self.receive_server_response(my_socket)
        self.handle_server_response(request, data)
    
    def send_and_recive(self,my_socket, request):
        if self.valid_request(request):
            self.send_request_to_server(my_socket, request)
            self.process_server_response(my_socket)
        else:
            raise Exception('Invalid command! fix your code!')
        
def main():
    # open socket with the server.
    print('\n')
    print('Alice \n')
    client = CLIENT()
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((IP, PORT))
    client.send_and_recive(my_socket, 'Client_Hello')
    client.process_server_response(my_socket)
    client.process_server_response(my_socket)
    client.process_server_response(my_socket)
    client.send_request_to_server(my_socket, 'Client_Send_Encrypted_Key')
    client.send_request_to_server(my_socket, 'Client_Change_Cipher_Spec')
    # client.send_request_to_server(my_socket, 'Client_Handshake_Finished')
    print('Close connection\n') 
    my_socket.close()


# %% Main

if __name__ == '__main__':
    main()