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

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    print("Waiting to receive messages...")
    while True:
        (data, address) = s.recvfrom(1024)
        print("Received message: " + data.decode())
        if data == b"exit":
            break
    s.close()

else:
    HOST = input("Entrez l'adresse IP du serveur : ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello, world")
        data = s.recv(1024)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while True:
            data = input("Enter message to send or type 'exit': ")
            s.sendto(data.encode(), HOST)
            if data == "exit":
                break

        s.close()

    print(f"Received {data!r}")
