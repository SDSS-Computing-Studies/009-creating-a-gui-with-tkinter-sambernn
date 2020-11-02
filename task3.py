import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)

label2 = tk.Label(window, text="Pochacco!")

label3 = tk.Label(window, text="A cuddly little puppy! This is from the same \n creators who brought you Keropi and Kero Kero", bg="CadetBlue1")

label1.grid(row = 1, column = 3, rowspan = 5)
label2.grid(row = 3, column = 4)
label3.grid(row = 6, column = 1, columnspan = 7)

window.mainloop()