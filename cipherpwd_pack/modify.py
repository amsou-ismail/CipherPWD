from getpass import getpass
import time

from clean import effacer_ecran

# Function to modify the data
def modifier_login_mdp(message_dechiffrer, userchoix, chemin):
    if userchoix == 4: 
        try:
            for i in range(9):
                print(f"\r Loading file "+"." * (i % 4) +"    ", end="")
                time.sleep(0.5)
            effacer_ecran()

            first_round = 0
            num_modification = -1
            while True:
                print("---------------  🛠️  Modify your data  🛠️  ---------------\n")
                print("\nHere is your data: \n")
                xt = 0
                p = 1
                for msg in message_dechiffrer:
                    if xt % 6 == 0:
                        print(f"Position ----->  {p} ")
                        p += 1
                    print(msg)
                    xt += 1
                print(f"\r🛠️  Enter the position of the login you want to modify ('0' to quit) : ", end="")
                num_modification = int(input())
                first_round += 1
                time.sleep(2)
                effacer_ecran()
                if num_modification == 0 and first_round == 1:
                    print(" \n No changes !!! ")
                    print("\n You can open your file to view your data ")
                    return message_dechiffrer
                elif num_modification == 0:
                    print("!!! You have exited !!! \n")
                    return message_dechiffrer
                elif num_modification < 0 or num_modification > p - 1:  # Ask the user which login or password they want to modify
                    print("\n❌ Invalid number. Please try again. ❌")
                    time.sleep(2)
                    effacer_ecran()
                    return modifier_login_mdp()
                else:
                    i = 0
                    index = (num_modification - 1) * 6
                    print("\nCurrent data: \n")
                    for i in range(4):
                        msg = message_dechiffrer[index + i]
                        print(msg)
                    choix_modification = int(input("\nDo you want to modify the (1) Login or (2) Password ? : "))

                    if choix_modification == 1:
                        nouveau_login = input("\nEnter the new login : ")
                        # Update the login at the correct position
                        message_dechiffrer[index + 1] = f"login: {nouveau_login}"

                    elif choix_modification == 2:
                        nouveau_mdp = getpass("\nEnter the new password : ")
                        # Update the password at the correct position
                        message_dechiffrer[index + 2] = f"password: {nouveau_mdp}"

                    else:
                        print("\n❌ Invalid choice. Please try again. ❌")
                        return modifier_login_mdp()

                # Rewrite the file with the modifications
                with open(chemin, "w") as fichier:
                    for msg in message_dechiffrer:
                        fichier.write(msg + "\n")

                print(f"\n✔️  The file '{chemin}' has been successfully updated!!!  ✔️")
                print("\n You can open your file to view your data ")
                time.sleep(2)
                effacer_ecran()

        except FileNotFoundError:
            print("\n❌ The specified file does not exist. Please try again. ❌")
            time.sleep(5)
            effacer_ecran()
        except Exception as e:
            print(f"❌ Error while processing the file: {e} ❌")
    return message_dechiffrer
