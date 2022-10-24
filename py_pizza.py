import tkinter as tk

root_window = tk.Tk()
root_window.title("Python Pizza Calculator")
root_window.geometry("600x400")

frm_left_frame = tk.Frame(root_window, borderwidth=50)
frm_left_frame.pack()

lbl_Title = tk.Label(frm_left_frame, text="Ovo je labela text1")
lbl_Title.pack()

btn_Reset = tk.Button(root_window, text="Reset")
btn_Reset.pack()

ent_size = tk.Entry(root_window)
ent_size.pack()

txt_description = tk.Text(root_window)
txt_description.pack()

rbtn_pizza_size_small = tk.Radiobutton(root_window, text="Small", value="1")
rbtn_pizza_size_small.pack()
rbtn_pizza_size_medium = tk.Radiobutton(root_window, text="Medium", value="2")
rbtn_pizza_size_medium.pack()
rbtn_pizza_size_large = tk.Radiobutton(root_window, text="Large", value="3")
rbtn_pizza_size_large.pack()

root_window.mainloop()