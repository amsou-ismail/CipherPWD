import hashlib
from getpass import getpass
import time

from choice import choix
from check import filecheck
from listing import listemessage
from encryption import chiffrement
from decryption import dechiffrement
from clean import effacer_ecran
from filling import remplissage
from modify import modifier_login_mdp
from delete import supprimer

# Here is the main code that calls the functions
while True:
    effacer_ecran()
    userchoix = choix() 
    if userchoix == 1:
        message, chemin = filecheck()
        messageliste = listemessage(message)
        userkey = getpass("\nEnter your encryption password  : ")
        key = hashlib.sha256(userkey.encode()).digest()[:16]
        message_chiffrer = []
        message_chiffrer = chiffrement(messageliste, key)
        with open(chemin, "w") as fichier:  # Open the file in write mode ("w" deletes the existing content)
            for msg in message_chiffrer:
                fichier.write(msg + "\n")
        print("\n✔️ The file has been successfully encrypted !!! ✔️")
        time.sleep(2)
        effacer_ecran()
    elif userchoix == 2 or userchoix == 6 or userchoix == 4:
        x = None
        message, chemin = filecheck()

        while x == None:
            try:
                messageliste = listemessage(message)
                userkey = getpass("\nEnter your decryption password : ")
                key = hashlib.sha256(userkey.encode()).digest()[:16]
                message_dechiffrer = []
                message_dechiffrer = dechiffrement(messageliste, key)
                x = True
            except (ValueError, KeyError):
                print("\n❌ Incorrect password. Please try again.")
                time.sleep(3)
                effacer_ecran()
                x = None

        with open(chemin, "w") as fichier:  # Open the file in write mode ("w" deletes the existing content)
            for msg in message_dechiffrer:
                fichier.write(msg + "\n")
        print("\n✔️ The file has been successfully decrypted !!! ✔️")

        ##upgrade##
        if userchoix == 6 or userchoix == 4:
            message_dechiffrer = supprimer(message_dechiffrer, userchoix, chemin)
            message_dechiffrer = modifier_login_mdp(message_dechiffrer, userchoix, chemin)
        ##upgrade##

        print("\n✔️ You can open your file to access your passwords ✔️")
        for i in range(30, -1, -1):
            print(f"\r⏳ It will be encrypted in {i} seconds ⏳", end="")
            time.sleep(1)
        effacer_ecran()  
        message_chiffrer = []
        message_chiffrer = chiffrement(message_dechiffrer, key)
        with open(chemin, "w") as fichier:  # Open the file in write mode ("w" deletes the existing content)
            for msg in message_chiffrer:
                fichier.write(msg + "\n")
        print("\n✔️ The file has been successfully encrypted !!! ✔️")
        time.sleep(2)
        effacer_ecran()
    elif (userchoix == 3 or userchoix == 5): 
        remplissage(userchoix)
        time.sleep(5)
        effacer_ecran()
    
# SAAD AND ISMAIL ARE THE BEST 
