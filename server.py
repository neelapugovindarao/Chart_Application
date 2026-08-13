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

