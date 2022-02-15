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
from Q68Client import AESCBC,SHA1_MAC
from Crypto.Random import get_random_bytes
from Crypto.Cipher.AES import block_size

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
        self.message_type_client_send_encrypted_key = bytearray.fromhex("10")[0]
        self.message_type_change_cipher_spec = bytearray.fromhex("14")[0]
        self.message_type_client_handshake_finished = bytearray.fromhex("fe")[0]
        self.message_type_client_close_notification = bytearray.fromhex("15")[0]
        self.k = 1024
        self.RSA = None
        self.e = None
        self.n = None
        self.d = None
        self.plainText = None
        self.key = None

    def decrypt_and_authenticate(self,cipherText,iv,mac):
        print('Decrypting received message:\n')
        self.symmetric_cipher = AESCBC(self.key,iv)
        plainText = self.symmetric_cipher.decrypt(cipherText)
        mac_computed = SHA1_MAC(self.key,plainText.decode())
        if mac_computed == mac:
            print('Received text: ' + str(plainText) + '\n')
        else:
            raise Exception('Decryption failed fix your code, mac is not valid!')

    def receive_client_request(self,client_socket):
        data = client_socket.recv(BUFFER_SIZE)
        if data[0] == self.message_type_change_cipher_spec:
            print_with_hexdump(data,'receive',True)
            request = 'Client_Change_Cipher_Spec'
        elif data[0] == self.message_type_client_close_notification:
            print_with_hexdump(data,'receive',True)
            request = 'Client_Close_Notification'
        elif data[5] == self.message_type_client_hello:
            print_with_hexdump(data,'receive',True)
            request = 'Client_Hello'
        elif data[5] == self.message_type_client_send_encrypted_key:
            print_with_hexdump(data,'receive')
            request = 'Client_Send_Encrypted_Key'
        elif data[5] == self.message_type_client_handshake_finished:
            request = 'Client_Handshake_Finished'
        else:
            raise Exception('Request is invalid! fix your code!')
        return request, data
            
    def check_client_request(self, data):
        if (int.from_bytes(data[3:5],'big') == len(data[5:])) & (int.from_bytes(data[6:9],'big') == len(data[9:])):
            return True
        else:
            return False
    
    def handle_client_request(self, request, data=None):
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
        elif request == 'Server_Certificate':
            print('Sending Server Certificate.\n')
            handshake_record =          bytearray.fromhex("16")
            protocol_version =          bytearray.fromhex("03 03")
            message_len =               bytearray.fromhex("03 2f")
            record_header =             handshake_record + protocol_version + message_len
            handshake_message_type =    bytearray.fromhex("0b")
            message_len_2 =             bytearray.fromhex("00 03 2b")
            handshake_header =          handshake_message_type + message_len_2
            certificates_len =          bytearray.fromhex("00 03 28") # if there are many certificates
            certificate_len =           bytearray.fromhex("00 03 25")
            certificate =               certificates_len + certificate_len
            certificate_sequence =      bytearray.fromhex("30 82 03 21")
            certificate_info_sequence = bytearray.fromhex("30 82 02 09")
            version =                   bytearray.fromhex("a0 03 02 01 02")
            serial_number =             bytearray.fromhex("02 08 15 5a 92 ad c2 04 8f 90")
            # SHA256 with RSA encryption, null params
            algorithm =                 bytearray.fromhex("30 0d 06 09 2a 86 48 86 f7 0d 01 01 0b 05 00")
            issuer_sequence =           bytearray.fromhex("30 22")
            # country US
            country =                   bytearray.fromhex("31 0b 30 09 06 03 55 04 06 13 02 55 53")
            organizational_unit =       bytearray.fromhex("31 13 30 11 06 03 55 04 0a 13 0a 45 78 61 6d 70 6c 65 20 43 41")
            # valid from date to date
            validity =                  bytearray.fromhex("30 1e 17 0d 31 38 31 30 30 35 30 31 33 38 31 37 5a 17 0d 31 39 31 30 30 35 30 31 33 38 31 37 5a")
            subject_sequence =          bytearray.fromhex("30 2b")
            country2 =                  bytearray.fromhex("31 0b 30 09 06 03 55 04 06 13 02 55 53")
            common_name =               bytearray.fromhex("31 1c 30 1a 06 03 55 04 03 13 13 65 78 61 6d 70 6c 65 2e 75 6c 66 68 65 69 6d 2e 6e 65 74")
            public_key =                bytearray.fromhex("30 82 01 22 30 0d 06 09 2a 86 48 86 f7 0d 01 01 01 05 00 03 82 01 0f 00 30 82 01 0a 02 82 01 01 00 c4 80 36 06 ba e7 47 6b 08 94 04 ec a7 b6 91 04 3f f7 92 bc 19 ee fb 7d 74 d7 a8 0d 00 1e 7b 4b 3a 4a e6 0f e8 c0 71 fc 73 e7 02 4c 0d bc f4 bd d1 1d 39 6b ba 70 46 4a 13 e9 4a f8 3d f3 e1 09 59 54 7b c9 55 fb 41 2d a3 76 52 11 e1 f3 dc 77 6c aa 53 37 6e ca 3a ec be c3 aa b7 3b 31 d5 6c b6 52 9c 80 98 bc c9 e0 28 18 e2 0b f7 f8 a0 3a fd 17 04 50 9e ce 79 bd 9f 39 f1 ea 69 ec 47 97 2e 83 0f b5 ca 95 de 95 a1 e6 04 22 d5 ee be 52 79 54 a1 e7 bf 8a 86 f6 46 6d 0d 9f 16 95 1a 4c f7 a0 46 92 59 5c 13 52 f2 54 9e 5a fb 4e bf d7 7a 37 95 01 44 e4 c0 26 87 4c 65 3e 40 7d 7d 23 07 44 01 f4 84 ff d0 8f 7a 1f a0 52 10 d1 f4 f0 d5 ce 79 70 29 32 e2 ca be 70 1f df ad 6b 4b b7 11 01 f4 4b ad 66 6a 11 13 0f e2 ee 82 9e 4d 02 9d c9 1c dd 67 16 db b9 06 18 86 ed c1 ba 94 21 02 03 01 00 01")
            extensions =                bytearray.fromhex("a3 52 30 50")
            extension_key_usage =       bytearray.fromhex("30 0e 06 03 55 1d 0f 01 01 ff 04 04 03 02 05 a0")
            extension_extend_key_usage= bytearray.fromhex("30 1d 06 03 55 1d 25 04 16 30 14 06 08 2b 06 01 05 05 07 03 02 06 08 2b 06 01 05 05 07 03 01")
            extension_auth_key_identity=bytearray.fromhex("30 1f 06 03 55 1d 23 04 18 30 16 80 14 89 4f de 5b cc 69 e2 52 cf 3e a3 00 df b1 97 b8 1d e1 c1 46")
            # SHA256 with RSA encryption, null params
            signature_algorithm2 =      bytearray.fromhex("30 0d 06 09 2a 86 48 86 f7 0d 01 01 0b 05 00")
            signature =                 bytearray.fromhex("03 82 01 01 00 59 16 45 a6 9a 2e 37 79 e4 f6 dd 27 1a ba 1c 0b fd 6c d7 55 99 b5 e7 c3 6e 53 3e ff 36 59 08 43 24 c9 e7 a5 04 07 9d 39 e0 d4 29 87 ff e3 eb dd 09 c1 cf 1d 91 44 55 87 0b 57 1d d1 9b df 1d 24 f8 bb 9a 11 fe 80 fd 59 2b a0 39 8c de 11 e2 65 1e 61 8c e5 98 fa 96 e5 37 2e ef 3d 24 8a fd e1 74 63 eb bf ab b8 e4 d1 ab 50 2a 54 ec 00 64 e9 2f 78 19 66 0d 3f 27 cf 20 9e 66 7f ce 5a e2 e4 ac 99 c7 c9 38 18 f8 b2 51 07 22 df ed 97 f3 2e 3e 93 49 d4 c6 6c 9e a6 39 6d 74 44 62 a0 6b 42 c6 d5 ba 68 8e ac 3a 01 7b dd fc 8e 2c fc ad 27 cb 69 d3 cc dc a2 80 41 44 65 d3 ae 34 8c e0 f3 4a b2 fb 9c 61 83 71 31 2b 19 10 41 64 1c 23 7f 11 a5 d6 5c 84 4f 04 04 84 99 38 71 2b 95 9e d6 85 bc 5c 5d d6 45 ed 19 90 94 73 40 29 26 dc b4 0e 34 69 a1 59 41 e8 e2 cc a8 4b b6 08 46 36 a0")
            data = record_header + handshake_header + certificate + certificate_sequence + certificate_info_sequence + version + serial_number + algorithm + issuer_sequence + country + organizational_unit + validity + subject_sequence + country2 + common_name + public_key + extensions + extension_key_usage + extension_extend_key_usage + extension_auth_key_identity + signature_algorithm2 + signature
        elif request == 'Server_Key_Exchange':
            self.RSA = RSAPCKS1PaddingOracle(self.k)
            sleep(2) # make sure data has time to move
            self.e = self.RSA.e
            self.n = self.RSA.n
            self.d = self.RSA.d
            print('Sending  Server Key Exchange.\n')
            handshake_record =          bytearray.fromhex("16")
            protocol_version =          bytearray.fromhex("03 03")
            message_len =               bytearray.fromhex("08 09")
            record_header =             handshake_record + protocol_version + message_len
            handshake_message_type =    bytearray.fromhex("0c")
            message_len_2 =             bytearray.fromhex("00 08 05")
            handshake_header =          handshake_message_type + message_len_2
            public_e =                  b'\x03' + long_to_bytes(self.e,2)
            public_n =                  bytearray.fromhex("01 00") + long_to_bytes(self.n,self.k*2)
            data = record_header + handshake_header + public_e + public_n
        elif request == 'Server_Hello_Done':
            print('Sending  Server Hello Done.\n')
            handshake_record =          bytearray.fromhex("16")
            protocol_version =          bytearray.fromhex("03 03")
            message_len =               bytearray.fromhex("00 04")
            record_header =             handshake_record + protocol_version + message_len
            handshake_message_type =    bytearray.fromhex("0e")
            message_len_2 =             bytearray.fromhex("00 00 00")
            handshake_header =          handshake_message_type + message_len_2
            data = record_header + handshake_header
        elif request == 'Client_Send_Encrypted_Key':
            print('Received client encrypted key.\n')
            handshake_record =          bytearray.fromhex("16")
            protocol_version =          bytearray.fromhex("03 03")
            message_len =               bytearray.fromhex("00 06")
            record_header =             handshake_record + protocol_version + message_len
            handshake_message_type =    bytearray.fromhex("ff") # new message type for padding failure or success
            message_len_2 =             bytearray.fromhex("00 00 02")
            handshake_header =          handshake_message_type + message_len_2
            message_len_3 =             bytearray.fromhex("01")
            cipherText = int.from_bytes(data[11:],'big')
            if self.RSA.padding_oracle(cipherText):
                valid_padding = bytearray.fromhex("01")
                self.plainText = self.RSA.decrypt(cipherText)
                self.key = self.RSA.remove_pkcs(long_to_bytes(self.plainText,self.k))[-16:]
                print('Decrypted plain text without padding: ' + str(self.key) + '\n')
            else:
                valid_padding = bytearray.fromhex("00")
            data = record_header + handshake_header + message_len_3 + valid_padding
        elif request == 'Client_Change_Cipher_Spec':
            print('Changing cipher spec.\n')
        elif request == 'Client_Handshake_Finished':
            print('Received client handshake finished.\n')
            iv = data[9:25]
            cipherText = data[25:57]
            mac = data[59:]
            self.decrypt_and_authenticate(cipherText,iv,mac)
            change_cipher_spec =        bytearray.fromhex("14") 
            protocol_version =          bytearray.fromhex("03 03")
            message_len =               bytearray.fromhex("00 01") 
            payload =                   bytearray.fromhex("01")
            data = change_cipher_spec + protocol_version + message_len + payload
            print('Sending server change cipher suit.\n')
        elif request == 'Server_Handshake_Finished':
            print('Send server handshake finished.\n')
            handshake_record =          bytearray.fromhex("16")
            protocol_version =          bytearray.fromhex("03 03")
            message_len =               bytearray.fromhex("00 4a")
            record_header =             handshake_record + protocol_version + message_len
            handshake_message_type =    bytearray.fromhex("fe")
            message_len_2 =             bytearray.fromhex("00 00 46")
            handshake_header =          handshake_message_type + message_len_2
            self.iv =                   get_random_bytes(block_size)
            self.symmetric_cipher =     AESCBC(self.key,self.iv)
            super_secret_message =      'Hello there GetZer0Dayed!!'
            encrypted_data =            self.symmetric_cipher.encrypt(super_secret_message) # 32 bytes
            mac_len =                   bytearray.fromhex("00 20")
            mac =                       SHA1_MAC(self.key,super_secret_message) # 20 bytes
            data = record_header + handshake_header + self.iv + encrypted_data + mac_len + mac
        elif request == 'Client_Close_Notification':
            print('Received client close notification.\n')
            data = data
        else:
            raise Exception('Request is invalid! fix your code!')
        return data
    
    def send_response_to_client(self,client_socket,data):
        if data[5] == bytearray.fromhex("ff")[0]:
            print_with_hexdump(data,'send')
        else:
            print_with_hexdump(data,'send',True)
        client_socket.send(data)

    def send_to_client(self,request,client_socket):
        data = self.handle_client_request(request)
        self.send_response_to_client(client_socket,data)

    def receive_and_send_response(self,client_socket):
        request, data = self.receive_client_request(client_socket)
        if self.check_client_request(data):
            data = self.handle_client_request(request, data)
            if request == 'Client_Change_Cipher_Spec': return True
            self.send_response_to_client(client_socket,data)
        else:
            raise Exception('Invalid request! request is not formatted correctly check your length')
       
    def receive_and_handle(self,client_socket):
        request, data = self.receive_client_request(client_socket)
        self.handle_client_request(request, data)
        
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
    server.send_to_client('Server_Certificate',client_socket)
    server.send_to_client('Server_Key_Exchange',client_socket)
    server.send_to_client('Server_Hello_Done',client_socket)
    while True:
        val = server.receive_and_send_response(client_socket)
        if val:
            break
    server.receive_and_send_response(client_socket)
    server.send_to_client('Server_Handshake_Finished',client_socket)
    server.receive_and_handle(client_socket)
    print('Client connected\n')
    print('Close connection\n')
    client_socket.close()
    server_socket.close()

# %% Main

if __name__ == '__main__':
    main()



