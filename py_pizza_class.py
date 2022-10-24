from tkinter import *
from tkinter import ttk

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.toppings = [
            "Sausage",
            "Pepperoni",
            "Chicken",
            "Mushroom",
            "Onion",
            "Black Olive",
            "Green Pepper",
            "Red Pepper"
        ]
        self.checkboxes = list(self.toppings)
        self.checkboxesVars = list(self.toppings)
        self.prices = {
            "medium": 9.99,
            "large": 13.99,
            "x-large": 14.99,
            "medium-toppings": 1.0,
            "large-toppings": 1.5,
            "xl-toppings": 1.8
        }
        self.price = 0
        self.create_widgets()


    def create_widgets(self):
        self.lbl_select_size = Label(self, text="Select pizza size:", foreground="#CD5C5C")
        self.lbl_select_size.grid(row=0, column=0, sticky=W)

        self.rb_size_value = StringVar()
        self.rb_medium = Radiobutton(self, text="Medium", value="medium", variable=self.rb_size_value)
        self.rb_medium.grid(row=1, column=0, sticky=W)
        self.rb_medium.select()
        self.rb_large= Radiobutton(self, text="Large", value="large", variable=self.rb_size_value)
        self.rb_large.grid(row=1, column=1, sticky=W)
        self.rb_xlarge = Radiobutton(self, text="Extra Large", value="x-large", variable=self.rb_size_value)
        self.rb_xlarge.grid(row=1, column=2, sticky=W)

        self.lbl_select_toppings = Label(self, text="Select Toppings:")
        self.lbl_select_toppings.grid(row=2, column=0, sticky=W)

        line = 2
        for i in range(len(self.toppings)):
            line += 1
            self.checkboxesVars[i] = BooleanVar()
            self.checkboxes[i] = Checkbutton(self, text=self.toppings[i], variable=self.checkboxesVars[i])
            self.checkboxes[i].grid(row=line, column=0, sticky=W)

        line += 1
        self.btn_reset = Button(self, text="Reset")
        self.btn_reset.grid(row=line, column=0)
        self.btn_calculate_price = Button(self, text="Calculate price", command=self.reset)
        self.btn_calculate_price.grid(row=line, column=1)

        line += 1
        self.lbl_total_price = Label(self, text="Total: ")
        self.lbl_total_price.grid(row=line, column=0, sticky=E)

        self.entry_total_price = Entry(self, width=10)
        self.entry_total_price.grid(row=line, column=1, sticky=W)

    def calculate_price(self):
        self.total_toppings = 0
        for i in range(len(self.toppings)):
            if self.checkboxesVars[i].get():
                self.total_toppings += 1

        self.price = self.prices[self.rb_size_value.get()] + (self.total_toppings + self.prices[self.rb_size_value.get() + " - toppings"])
        self.entry_total_price.delete(0, END)
        self.entry_total_price.insert(END, f"{self.price:.2f}")

    def reset(self):
        self.rb_medium.select()
        for i in range(len(self.toppings)):
            self.checkboxes[i].deselect()
        self.entry_total_price.delete(0, END)

    def display_price(self):
        varText = self.entry_total_price.get()
        varReplaced = varText.upper()
        self.entry_total_price.delete(0, END)
        self.entry_total_price.insert(END, varReplaced)


window = Tk()
window.title("Python Pizza Calculator")
window.geometry("300x400")

app = Application(window)
app.mainloop()