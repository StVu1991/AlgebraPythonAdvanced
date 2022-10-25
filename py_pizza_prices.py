import sqlite3
from tkinter import *
from db_repo import update_data

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.prices = {
            "medium": 0,
            "large": 0,
            "x-large": 0,
            "medium-toppings": 0,
            "large-toppings": 0,
            "x-large-toppings": 0,
        }

        self.conn = sqlite3.connect("pizza.db")
        self.cursor = self.conn.cursor()

        sql_select_prices = "SELECT product, price FROM prices"
        for row in self.cursor.execute(sql_select_prices):
            self.prices[row[0]] = row[1]
            print(row)


        self.conn.close()

        for k, v in self.prices.items():
            print(k, v)

        self.create_widgets()

    def create_widgets(self):
        self.lbl_title = Label(self, text="Pizza Calculator Prices")
        self.lbl_title.grid(row=0, column=0, columnspan=2, sticky=W, padx=10, pady=10)

        self.lbl_tbl_size_title = Label(self, text="Size")
        self.lbl_tbl_size_title.grid(row=0, column=0)
        self.lbl_toppings_title = Label(self, text="Toppings")
        self.lbl_tbl_size_title.grid(row=0, column=1, sticky=W)

        self.lbl_medium = Label(self, text="Medium")
        self.lbl_medium.grid(row=1, column=1, sticky=E)
        self.entry_medium_size = Entry(self, width=10)
        self.entry_medium_size.insert(END, f"{self.prices['medium']:.2f}")
        self.entry_medium_size.grid(row=1, column=2)
        self.entry_medium_toppings = Entry(self, width=10)
        self.entry_medium_toppings.grid(row=2, column=2)
        self.entry_medium_size.insert(END, f"{self.prices['medium-toppings']:.2f}")


        self.lbl_large = Label(self, text="Large")
        self.lbl_large.grid(row=3, column=0, sticky=E)
        self.entry_large_size= Entry (self, width=10)
        self.entry_large_size.insert(END, f"{self.prices['large']:.2f}")
        self.entry_large_size.grid(row=3, column=1)
        self.entry_large_toppings = Entry(self, width=10)
        self.entry_large_toppings.grid(row=3, column=2)
        self.entry_large_toppings.insert(END, f"{self.prices['large-toppings']}")

        self.lbl_x_large = Label(self, text="Extra Large")
        self.lbl_x_large.grid(row=4, column=0, sticky=E)
        self.entry_x_large_size = Entry (self, width=10)
        self.entry_x_large_size.insert(END, f"{self.prices['x-large']:.2f}")
        self.entry_x_large_size.grid(row=4, column=1)
        self.entry_x_large_toppings = Entry(self, width=10)
        self.entry_x_large_toppings.grid(row=4, column=2)
        self.entry_x_large_toppings.insert(END, f"{self.prices['x-large-toppings']:.2f}")

        self.btn_update = Button(self, text="Update", command=self.update)
        self.btn_update.grid(row=5, column=1, pady=10)

        self.lbl_update_info_var = StringVar()
        self.lbl_update_info_var.set('')
        self.lbl_update_info = Label(self, textvariable=self.lbl_update_info_var, foreground="#07BF23")
        self.lbl_update_info.grid(row=6, column=0, columnspan=2, pady=5)

    def update(self):
        self.prices["medium"] = self.entry_medium_size.get()
        self.prices["large"] = self.entry_large_size.get()
        self.prices["x-large"] = self.entry_x_large_size.get()
        self.prices["medium-toppings"] = self.entry_medium_toppings.get()
        self.prices["large-toppings"] = self.entry_large_toppings.get()
        self.prices["x-large-toppings"] = self.entry_x_large_toppings.get()

        for product, price in self.prices.items():
            sql_update_price = "UPDATE prices SET price = ? WHERE product = ?"
            data = (product, price)

            update_result = update_data(sql_update_price, data)

        if update_result != 0:
            self.lbl_update_info_var.set(f"ERROR:")

           # self.cursor.execute("UPDATE prices SET price = ? WHERE product = ?", (price, product))
        #self.conn.commit()

        self.lbl_update_info_var.set("Price update successfully!")

window = Tk()
window.title("STARA SAVA - Python Pizza Prices")
window.geometry("300x300")

app = Application(window)
app.mainloop()