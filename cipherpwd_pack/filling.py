import hashlib
from getpass import getpass
import time
from clean import effacer_ecran
from encryption import chiffrement
from decryption import dechiffrement
from choice import choix
from listing import listemessage

# Function that will create a new encrypted file or add to an existing file
def remplissage(userchoix):
    data = []  # Initialize the data list
    motif = []  # Initialize the motif list
    userkey = None  # Initialize userkey before using it

    # Create a new file
    if userchoix == 5:
        i = 1
        chemin = input('\nEnter the path where you want to store your file (Don\'t forget the .txt extension, and use "/" for Linux paths or "\\" for Windows paths)  : ')

        while True:
            login = input(f"\nEnter login N°{i} ('stop' to stop) : ")

            if login.lower() == 'stop':
                if i == 1:
                    print("\n❌ You haven’t entered any data. ❌")
                    return choix()

                userkey = getpass("\n\nPlease enter the password to encrypt (To cancel the operation, enter anything you want) : ")
                if userkey == "":
                    print("\n❌❌Operation canceled. No password provided.❌❌")
                    time.sleep(5)
                    effacer_ecran()
                    return choix()

                key = hashlib.sha256(userkey.encode()).digest()[:16]

                try:
                    with open(chemin, "w") as fichier:
                        for idx, (login, passwd) in enumerate(data):
                            tiret = str('-' * ((70 - len(motif_temp)) // 2))
                            if ((70 - len(motif_temp)) % 2) == 0 :  
                                fichier.write(tiret + motif[idx] + tiret + "|\n")
                            else : 
                                fichier.write(tiret + motif[idx] + tiret + "-|\n")
                            fichier.write(f"login   : {login}\n")
                            fichier.write(f"password : {passwd}\n")
                            fichier.write("----------------------------------------------------------------------|\n\n\n")

                    with open(chemin, "r") as fichier:
                        message = fichier.read()

                    messageliste = listemessage(message)

                    message_chiffrer = chiffrement(messageliste, key)

                    with open(chemin, "w") as fichier:
                        for msg in message_chiffrer:
                            fichier.write(msg + "\n")

                    print(f"\n✔️  The file '{chemin}' has been created and encrypted successfully!!!  ✔️")
                    break

                except Exception as e:
                    print(f"\n❌ Error while writing to the file: {e} ❌")
                    time.sleep(5)
                    effacer_ecran()
                    break

            passwd = getpass(f"Enter the password for login N°{i} : ")
            motif_temp = input("Enter the associated motif (e.g. Instagram, Facebook...) : ")
            motif.append(motif_temp)
            data.append((login, passwd))
            i += 1

    # Add to an existing file
    elif userchoix == 3:
        chemin = input("\nEnter the path of the file to modify  : ")

        try:
            with open(chemin, "r") as fichier:
                message = fichier.read()
            messageliste = listemessage(message)

            userkey = getpass("\nPlease enter the password to decrypt : ")
            if userkey == "":
                print("\n❌❌Operation canceled. No password provided.❌❌")
                time.sleep(5)
                effacer_ecran()
                return remplissage()

            key = hashlib.sha256(userkey.encode()).digest()[:16]

            message_dechiffrer = dechiffrement(messageliste, key)

            print("\nHere are the old data: \n")
            for msg in message_dechiffrer:
                print(msg)
            for i in range(10, -1, -1):
                print(f"\r ⚠️ Your data will be cleared in {i} seconds... ⚠️   ", end="")
                time.sleep(1)
            effacer_ecran()

            i = int(len(message_dechiffrer) / 5) + 1
            while True:
                login = input(f"\nEnter login N°{i} to add ('stop' to stop) : ")
                if login.lower() == 'stop':
                    break

                passwd = getpass(f"Enter the password for login N°{i} : ")
                motif_temp = input("Enter the associated motif (e.g. Instagram, Facebook...) : ")
                motif.append(motif_temp)
                tiret = str('-' * ((70 - len(motif_temp)) // 2))
                if ((70 - len(motif_temp)) % 2) == 0 :                      
                    message_dechiffrer.append(tiret + motif_temp + tiret + "|")
                else : 
                    message_dechiffrer.append(tiret + motif_temp + tiret + "-|")
                message_dechiffrer.append(f"login    : {login}")
                message_dechiffrer.append(f"password : {passwd}")
                message_dechiffrer.append("----------------------------------------------------------------------|\n\n")
                i += 1

            message_chiffrer = chiffrement(message_dechiffrer, key)

            with open(chemin, "w") as fichier:
                for msg in message_chiffrer:
                    fichier.write(msg + "\n")

            print(f"\n✔️  The file '{chemin}' has been updated and encrypted successfully!!!  ✔️")

        except FileNotFoundError:
            print("\n❌ The specified file does not exist. Please try again. ❌")
            time.sleep(5)
            effacer_ecran()
        except Exception as e:
            print(f"❌ Error while processing the file: {e} ❌")
