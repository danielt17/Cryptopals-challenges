# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 18:41:12 2021

@author: danie
"""

# %% Challange

# https://cryptopals.com/sets/2/challenges/10

# %% Imports

from base64 import b64decode
from Crypto.Cipher import AES
from Q21 import PKCS7padding, PKCS7unpadding

# %% Functions

def xor(bitSeq1, bitSeq2):
    Xored = bytes([int(_a) ^ int(_b) for _a, _b in zip(bitSeq1, bitSeq2)])
    return Xored

def aes_ecb_encrypt_padded(ptext,Key):
    AES_ECB_cipher = AES.new(Key,AES.MODE_ECB)
    ciphertext = AES_ECB_cipher.encrypt(PKCS7padding(ptext,AES.block_size))
    return ciphertext
    
def aes_ecb_decrypt_padded(ctext,Key):
    AES_ECB_cipher = AES.new(Key,AES.MODE_ECB)
    plaintext = PKCS7unpadding(AES_ECB_cipher.decrypt(ctext),AES.block_size)
    return plaintext

def aes_cbc_encrypt(plainText, Key, Iv):
    cipherText = b''
    Ci = Iv
    for i in range(len(plainText)//AES.block_size):
        Pi = PKCS7padding(plainText[i*AES.block_size:(1+i)*AES.block_size],AES.block_size)
        Ci = aes_ecb_encrypt_padded(xor(Pi,Ci),Key)
        cipherText = cipherText + Ci
    return cipherText

def aes_cbc_decrypt(cipherText, Key, Iv, unpad=True):
    plaintext = b''
    Ci = Iv
    for i in range(len(cipherText)//AES.block_size):
        curCipherTextBlock = cipherText[i*AES.block_size:(1+i)*AES.block_size]
        Pi = xor(aes_ecb_decrypt_padded(curCipherTextBlock,Key),Ci)
        Ci = curCipherTextBlock
        plaintext = plaintext + Pi
    return plaintext

# %% Main

if __name__ == '__main__':
    print('\n')
    with open('22.txt') as f:
        cipherText = b64decode(f.read())
    Iv = b'\x00' * AES.block_size
    Key = "YELLOW SUBMARINE".encode("utf8")
    plainText = aes_cbc_decrypt(cipherText, Key, Iv)
    print('Decrypted text: \n\n' + str(plainText.decode()))
    ciphertextrebuilt = str(aes_cbc_encrypt(plainText,Key, Iv))
    if ciphertextrebuilt == str(cipherText):
        print('\n')
        print('Encrypt decrypt chain was successfully built. \n')
    else:
        print('\n Fail \n')
    
