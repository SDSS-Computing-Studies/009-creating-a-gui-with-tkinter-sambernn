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

prev = tk.Button(window, text="< Previous")
save = tk.Button(window, text="Save Entry")
nex = tk.Button(window, text="Next >")

label1.grid(row=1,column=1, sticky=W)
button1.grid(row=1,column=2, sticky=E)
entry1.grid(row=1,column=3, sticky=E)
label2.grid(row=2,column=1)

name.grid(row=3, column=1)
typ.grid(row=3, column=2)
breed.grid(row=3, column=3)
owner.grid(row=3, column=4)
birthdate.grid(row=3, column=5)

enter1.grid(row=4, column=1)
enter2.grid(row=4, column=2)
enter3.grid(row=4, column=3)
enter4.grid(row=4, column=4)
enter5.grid(row=4, column=5)

prev.grid(row=5, column=1, sticky=W)
save.grid(row=5, column=2)
nex.grid(row=5, column=3, sticky=E)

window.mainloop()