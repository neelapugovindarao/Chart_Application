import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

name = input("Enter your name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
