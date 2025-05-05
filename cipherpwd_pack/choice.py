import time
import clean




#Function to verify the user's choice
def choix() :
    userchoix = int(input("""
1. Encryption				🔐 :
2. Decryption				🔓 :
3. Add to an existing file		➕ :
4. Modify a password or login		🔧 :	
5. Create a new file			📝 :
6. Delete passwords			🚫 :
7. Exit					👋 :
------------------------------------------->   """))
    if userchoix!=1 and userchoix!=2 and userchoix!=3 and userchoix!=4 and userchoix!=5 and userchoix != 6 and userchoix!=7 :
        print("\n     ❌ Invalid choice ! ❌\n")
        time.sleep(2)
        clean.effacer_ecran()
        return choix()
    elif userchoix == 7 :
        clean.exit_program()
    else :
        return userchoix