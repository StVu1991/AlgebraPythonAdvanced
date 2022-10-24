from tkinter import *

class DevFormApp(Frame):
    def __init__(self, master):
        super(DevFormApp, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        menubar = Menu(self)
        file_menu = Menu(menubar)
        file_menu.add_command(label="Submit", command=self.process)
        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_command(label="Quit", command=window.quit)


        self.lbl_message = Label(self, text="Instrukcije dostavljaču")
        self.lbl_message.grid(row=0, column=0, sticky=W)

        self.entry_message= Entry(self, width=50)
        self.entry_message.grid(row=1, column=0)

        self.btn_submit = Button(self, text="Submit", command=self.process)
        self.btn_submit.grid(row=1, column=1)

        self.delivery_info_msg = StringVar()
        self.delivery_info_msg.set("INIT PORUKA")
        self.lbl_delivery_info_msg = Label(self, textvariable=self.delivery_info_msg, foreground="#FF0000")

        self.lbl_delivery_info_msg.grid(row=2, column=0)

        window.config(menu=menubar)

    def process(self):
        delivery_instruction = self.entry_message.get()
        output_message = f"Poruka dostavljaču: {delivery_instruction}"
        print(output_message)
        self.delivery_info_msg.set(output_message)
        self.entry_message.delete(0, END)

window = Tk()
window.title("Delivery Form")
window.geometry("600x200")

app = DevFormApp(window)
app.mainloop()