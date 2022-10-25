import socket
import sqlite3
import json

conn = sqlite3.connect("pizza.db")
cursor = conn.cursor()

toppings = list()
sql_select_toppings = "SELECT topping FROM toppings ORDER BY topping"
for row in cursor.execute(sql_select_toppings):
    toppings.append(row[0])
toppings_to_send = str.encode(json.dumps(toppings))

prices = {
    "medium": 0,
    "large": 0,
    "x-large": 0
}
sql_select_prices = "SELECT product, price FROM prices"
for row in cursor.execute(sql_select_prices):
    prices[row[0]] = row [1]
prices_to_send = str.encode(json.dumps(prices))

#print(json.dumps(prices))

conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 8000
server.bind((host, port))
server.listen(5)

while True:
    print("Waiting for client to connection ... ")
    client, addr = server.accept()

    print(f"Accepted connection from {addr}")
    client.send(str.encode("Welcome to Pizza Calc Server"))

    while True:
        data_from_client = client.recv(1024)
        str_data_from_client = bytes.decode(data_from_client)

        if str_data_from_client == "toppings":
            print(" -- Sending toppings list to client -- ")
            client.send(toppings_to_send)
        elif str_data_from_client == "prices":
            print(" -- Sending prices list to client -- ")
            client.send(prices_to_send)
        elif str_data_from_client == "exit":
            print(" -- Disconnecting client -- ")
            break
        else:
            print(f" -- Recieved from client: {str_data_from_client} -- ")
            client.send(str.encode("Invalid command!"))

    client.close()