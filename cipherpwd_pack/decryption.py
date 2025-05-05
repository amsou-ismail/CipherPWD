from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64





#Decryption function
def dechiffrement(messageliste, key):
    liste_dechiffrement = []

    message_chif_byte = base64.b64decode(messageliste[0])   #Decode the encrypted message 
    iv = message_chif_byte[:AES.block_size]  #Extract the vector of initialisation (IV)
    dechif_aes = AES.new(key, AES.MODE_CBC, iv)  # Creating an object AES for the encryption with l'IV
    for i in messageliste:
        message_chif_byte = base64.b64decode(i)  # Decode the encrypted message 
        message_chif = message_chif_byte[AES.block_size:]  # Extract the encrypted message
        dechif = unpad(dechif_aes.decrypt(message_chif), AES.block_size).decode()  # take of  the padding
        liste_dechiffrement.append(dechif)
    return liste_dechiffrement
