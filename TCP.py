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
    HOST = gethostbyname('0.0.0.0')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
else:
    HOST = input("Entrez l'adresse IP du serveur : ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(input())
        data = s.recv(1024)

    print(f"Received {data!r}")
