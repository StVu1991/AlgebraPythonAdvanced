import sqlite3
from tkinter import *

class Application(Frame):
    def __init__(self, master):

        self.grid()
        self.toppings=[]
        self.prices={
            "medium": 0,
            "large": 0,
            "x-large": 0,
            "medium-toppings": 0,
            "large-toppings": 0,
            "x-large-toppings": 0
        }
        self.price = 0

        self.conn = sqlite3.connect("pizza.db")
        self.cursor = self.conn.cursor()

        sql_select_toppings = "SELECT topping FROM toppings ORDER BY topping"
        for row in self.cursor.execute(sql_select_toppings):
            self.toppings.append(row[0])

        sql_select_prices = "SELECT product, price FROM prices"
        for row in self.cursor.execute(sql_select_prices):
            self.prices[row[0]]=row[1]

        self.conn.close()

        self.checkboxes = list(self.toppings)
        self.checkboxesVar
