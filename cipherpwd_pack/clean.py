import os
from banner import afficher_banniere
import sys




#Function to clear the screen based on the operating system
def effacer_ecran():
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for macOS/Linux
        os.system('clear')
    afficher_banniere()


#Function to quit the programm based on the os 
def exit_program():
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for macOS/Linux
        os.system('clear')
    print("closing programm..👋")
    
    sys.exit()
