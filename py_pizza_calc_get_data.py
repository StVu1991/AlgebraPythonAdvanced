import sqlite3

class GetPPCData:
    def __init__(self):
        self.conn = sqlite3.connect("pizza.db")
        self.cursor = conn.cursor()

    def get_toppings(self):
        self.toppings = list()


        def get_toppings(self):
            self.toppings = list()

        sql_select_toppings = "SELECT topping FROM toppings ORDER BY topping"