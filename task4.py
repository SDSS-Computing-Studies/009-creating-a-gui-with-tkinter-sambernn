import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()

window.geometry("260x135")



dogphoto = PhotoImage(file="dog.png")
label = tk.Label(window, image=dogphoto)
label1 = tk.Label(window, text = "Pochacco!")

label2 = tk.Label(window, text = "A cuddly little puppy! This is from the same \n creators who brought you Keropi and Kero Kero", bg = "CadetBlue1")

label.place(x = 65, y = 0)
label1.place(x = 140, y = 40)
label2.place(x = 0, y = 100)

window.mainloop()
