from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import base64
from getpass import getpass
import os
import time





#FEncryption function
def chiffrement(messageliste,key) :
    chif_aes = AES.new(key,AES.MODE_CBC) # Create an AES object with the key in cbc mode
    liste_chiffrement = []
    for i in messageliste :
            message_pad = pad(i.encode(),AES.block_size)    # Add  padding to the  message
            chif = chif_aes.encrypt(message_pad)    # Message encryption
            message_chif_base64 = base64.b64encode(chif_aes.iv + chif).decode() #lThe encrypted message with the VI for decryption later 
            liste_chiffrement.append(message_chif_base64)
    return liste_chiffrement
