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
from socket import *

PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
isServer = input("Serveur (1) ou client(0) ?")



if isServer == "1":
    # HOST = gethostbyname('0.0.0.0')


    host = gethostbyname('0.0.0.0')
    port = 10000
    buf = 1024

    address = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.bind(address)

    print("Waiting to receive messages...")

    while True:
        (data, address) = UDPSock.recvfrom(buf)
        print("Received message: " + data.decode())
        if data == b"exit":
            break

    UDPSock.close()

else:
    # HOST = input("Entrez l'adresse IP du serveur : ")

    host = input("Entrez l'adresse IP du serveur : ")  # set to IP address of target computer
    port = 10000
    addr = (host, port)

    UDPSock = socket(AF_INET, SOCK_DGRAM)

    while True:
        data = input("Enter message to send or type 'exit': ")
        UDPSock.sendto(data.encode(), addr)
        if data == "exit":
            break

    UDPSock.close()
