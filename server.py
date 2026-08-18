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


def receive():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()

        print("Server is running...")

        while True:
            client, address = server.accept()
            print(f"Connected with {str(address)}")

            client.send("NAME".encode())
            name = client.recv(1024).decode()


