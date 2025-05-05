import time
from clean import effacer_ecran





#Function to delete some data from an encrypted file 
def supprimer(message_dechiffrer,userchoix,chemin) :
    if userchoix == 6 :
        for i in range(9) :
            print(f"\r Loading the file"+"." * (i%4) +"    ", end="")
            time.sleep(0.5)
        effacer_ecran()
        print("--------------- 🗑️ Delete passwords 🗑️---------------\n")
        print("\nHere is your data : \n")
        xt = 0
        p = 1
        for msg in message_dechiffrer:
            if xt%6==0 :
                print(f"Position ----->  {p} ")
                p+=1
                
            print(msg)
            xt+=1
        del_list = []
        xmtp = -1
        i=1
        while xmtp != 0 :
            print(f"\r🗑️ Enter the position of the login you want to delete (press \'0\' to quit):: " , end="")
            xmtp = int(input())
            del_list.append(xmtp)
            i+=1
        if del_list[0] == 0 :
            print(" \n No changes !!! ")
            print("\n You can now open your file to see your data  ")
            return message_dechiffrer
        del_list.sort(reverse=True) #Sort the numbers entered by the user in descending order to avoid the index problem

        for i in del_list :
            del_i = i*6 -1
            new_list = []
            j=-1
            for msg in message_dechiffrer :
                j+=1
                if j!=del_i and j!=del_i-1 and j!=del_i-2 and j!=del_i-3 and j!=del_i-4 and j!=del_i-5 :
                    new_list.append(msg)
            message_dechiffrer = new_list
        with open(chemin,"w") as fichier : #Open the file in write mode ("w" deletes the existing content)
            for msg in message_dechiffrer :
                fichier.write(msg + "\n")
        print("\n✔️  Your file has been modified succesfully !!! ✔️")
        print("\n Open your file to see your data ")
    return message_dechiffrer
