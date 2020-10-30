import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
 
nF = Frame()

entry1 = tk.Entry(window)

label1 = tk.Label(window,text="x")

entry2 = tk.Entry(window)

button1 = tk.Button(window,text="=")
 
entry3 = tk.Entry(window)

nF.pack()
entry1.pack(side=LEFT)
label1.pack(side=LEFT)
entry2.pack(side=LEFT)
button1.pack(side=LEFT)
entry3.pack(side=LEFT)
window.mainloop()
