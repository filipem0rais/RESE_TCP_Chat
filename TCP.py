import socket
from _socket import gethostbyname

'''
    Fichier: TCP.py
    Auteur: Filipe Dias Morais & Luca Böhlen
    Date création: 08.03.2022
    Python Version: 3.9
    
    Objectif :     Transmission alternative de messages entre deux clients en TCP.
    Commentaire :
'''

PORT = 10000
BUFFER = 1024
CHAR_FORMAT = "UTF-8"
isServer = input("Serveur (1) ou client(0) : ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # permet de choisir si le terminal est le client ou le serveur
# (utilisé pour initier la connexion)

if isServer == "1":
    host = gethostbyname('0.0.0.0')
    s.bind((host, PORT))
    s.listen(5)
    conn, addr = s.accept()
    print("Adresse utilisée pour la connection : " + addr[0])
    print("Port utilisé pour la connection : " + addr[1])
    conn.sendall(b"Bienvue sur le chat !")
    while True:
        data = conn.recv(BUFFER)
        print(data.decode(CHAR_FORMAT))
        if not data:
            break
        msg = input("Message : ")
        bMsg = msg.encode(CHAR_FORMAT)
        conn.sendall(bMsg)
    conn.close()
else:
    host = input("Entrez l'adresse IP du serveur : ")  # adresse IP du serveur
    s.connect((host, PORT))
    data = s.recv(BUFFER)
    print(data.decode(CHAR_FORMAT))
    while True:
        msg = input("Message : ")
        if msg == 'quit':  # permet de mettre fin à la transmission
            break
        bMsg = msg.encode(CHAR_FORMAT)
        s.sendall(bMsg)
        data = s.recv(1024)
        print(data.decode(CHAR_FORMAT))
    s.close()
