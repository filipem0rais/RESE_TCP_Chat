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

PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
isServer = input("Serveur (1) ou client(0) ?")

if isServer == "1":
    # HOST = gethostbyname('0.0.0.0')
    host = gethostbyname('0.0.0.0')
    # port = 10000
    # buf = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, 9999))
    s.listen(5)
    conn, addr = s.accept()

    conn.sendall(b"Bienvue sur le chat !")
    while True:
        data = conn.recv(1024)
        print(data.decode("ascii"))
        if not data:
            break
        msg = input("Message : ")
        bMsg = msg.encode("ascii")
        conn.sendall(bMsg)
    conn.close()

else:
    # HOST = input("Entrez l'adresse IP du serveur : ")

    # host = input("Entrez l'adresse IP du serveur : ")  # set to IP address of target computer
    # port = 10000
    # addr = (host, port)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("Entrez l'adresse IP du serveur : ")  # set to IP address of target computer
    s.connect((host, 9999))
    data = s.recv(1034)
    print(data.decode("ascii"))

    while True:
        msg = input("Message : ")
        if msg == 'quit':
            break
        bMsg = msg.encode("ascii")
        s.sendall(bMsg)
        data = s.recv(1024)
        print(data.decode("ascii"))

    s.close()
