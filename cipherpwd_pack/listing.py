





#Function to list The file 
def listemessage(message):
    x = ''
    messageliste = []
    for i in message:
        if i != "\n":  
            x += str(i)
        else:  
            messageliste.append(x)
            x = ''  

    if x: 
        messageliste.append(x)

    return messageliste
