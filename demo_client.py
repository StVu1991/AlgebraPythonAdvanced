import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname("localhost")
port = 8000

s.connect((host, port))

s.send(str.encode("Pozdrav od klijenta!"))