'''
    Fichier: TCP.py
    Auteur: Filipe Dias Morais
    Date création: 08.03.2022
    Python Version: 3.9
    
    Objectif : 
    Commentaire : 


Algorithme :
--------------


'''
from _socket import gethostbyname

'''
Programme principal
-------------------
'''
import socket

port = 10000
buffer = 1024
charFormat = "UTF-8"
isServer = input("Serveur (1) ou client(0) : ")

if isServer == "1":
    host = gethostbyname('0.0.0.0')


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    conn, addr = s.accept()
    print("Adresse utilisée pour la connection : "+addr[0])
    print("Port utilisé pour la connection : " + addr[1])
    conn.sendall(b"Bienvue sur le chat !")
    while True:
        data = conn.recv(buffer)
        print(data.decode(charFormat))
        if not data:
            break
        msg = input("Message : ")
        bMsg = msg.encode(charFormat)
        conn.sendall(bMsg)
    conn.close()

else:
    port = 10000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("Entrez l'adresse IP du serveur : ")  # set to IP address of target computer
    s.connect((host, port))
    data = s.recv(buffer)
    print(data.decode(charFormat))

    while True:
        msg = input("Message : ")
        if msg == 'quit':
            break
        bMsg = msg.encode(charFormat)
        s.sendall(bMsg)
        data = s.recv(1024)
        print(data.decode(charFormat))
    s.close()
