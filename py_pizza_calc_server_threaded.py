import socket
import sqlite3
import json
import threading

class ClientThread(threading.Thread):
    def __init__(self, client, addr):
        threading.Thread.__init__(self)
        self.client = client
        self.addr = addr

    def run(self):
        print(f"Accepted connection from {self.addr}")
        self.client.send(str.encode("Pozdrav od servera!"))

        while True:
            print(f"Waiting command from Client {self.addr}")
            data_from_client = self.client.recv(1024)
            str_data_from_client = bytes.decode(data_from_client)

        if str_data_from_client == "toppings":

conn = sqlite3.connect("pizza.db")
cursor = conn.cursor()

toppings = list()
sql_select_toppings = "SELECT topping FROM toppings ORDER BY topping"
for row in cursor.execute(sql_select_toppings)

host = ""
port = 8000
servwer.bind((host, port))
server.listen(5)

while True:
    print("Waiting for client connection ...")
    client, addr = server.accept()

    print(f"Accepted connection")
