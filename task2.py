import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.geometry("500x200")

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)

entry1 = tk.Entry(window)

button1 = tk.Button(window, text="Search by name")

label2 = tk.Label(window, text="Client Database")

name = tk.Label(window, text="Name")
typ = tk.Label(window, text="Type")
breed = tk.Label(window, text="Breed")
owner = tk.Label(window, text="Owner")
birthdate = tk.Label(window, text="Birthdate")

enter1 = tk.Entry(window)
enter2 = tk.Entry(window)
enter3 = tk.Entry(window)
enter4 = tk.Entry(window)
enter5 = tk.Entry(window)

label1.place(x=0,y=200)
entry1.place(x=500,y=200)
button1.place(x=400,y=200)
label2.place(x=250,y=150)

name.grid(row=1, column=1)
typ.grid(row=1, column=2)
breed.grid(row=1, column=3)
owner.grid(row=1, column=4)
birthdate.grid(row=1, column=5)

enter1.grid(row=2, column=1)
enter2.grid(row=2, column=2)
enter3.grid(row=2, column=3)
enter4.grid(row=2, column=4)
enter5.grid(row=2, column=5)

window.mainloop()