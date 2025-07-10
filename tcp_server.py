#!/usr/bin/python python

import socket 
import threading

host = "0.0.0.0"
port = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host,port))

server.listen(1)

print(f"[**] Server Started on : {host}:{port}......")

def handle_client(client_socket):
	while True:
		msg = client_socket.recv(1094).decode("utf-8")
		print(f"Message receive from {addr[0]}:{addr[1]}")
		print(f"Message is :-> {msg}\n")
		msg_send = input()
		client_socket.send(msg_send.encode('utf-8') + b'\n')

while True:
	client, addr = server.accept()
	print(f"Accept Connection from: {addr[0]}:{addr[1]}")
	client_handle = threading.Thread(target=handle_client,args=(client,))
	client_handle.start()


