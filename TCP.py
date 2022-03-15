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
import socket
import threading

clients = []
nicknames = []
# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

def receiveClient():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))
'''
Programme principal
-------------------
'''


PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
isServer = input("Serveur (1) ou client(0) ?")

if isServer == "1":
    # HOST = gethostbyname('0.0.0.0')

    '''
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
    '''
    host = "127.0.0.1"
    port = 55555
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()



else:
    # Choosing Nickname
    nickname = input("Choose your nickname: ")

    # Connecting To Server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 55555))
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()