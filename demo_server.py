import socket
import socket as socker

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 8000
server.bind((host, port))
server.listen(5)

while True:
    print("Waiting for client to connect ...")
    client, add = server.accept()
    data = client.recv(1024)
    string_data = bytes.decode(data)
    print(string_data)