import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

clients = []
names = []

# Broadcast message to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handle each client
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = names[index]
            broadcast(f"{name} left the chat!".encode())
            names.remove(name)
            break
