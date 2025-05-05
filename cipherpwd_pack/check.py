from clean import effacer_ecran
import time



#Function to get the file path and verify it with the file content
def filecheck() :
    while True :
        try:
            chemin = input("\nEnter the file path : ")
            with open(chemin , "r") as file:
                message = list(file.read())
            return message,chemin
        except FileNotFoundError :
            print("\n❌ Incorrect path. Please try again. ❌")
            time.sleep(5)
            effacer_ecran()
