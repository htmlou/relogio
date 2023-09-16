from tkinter import *
from tkinter import *

from time import strftime

root = Tk ()
root.title("Relógio DIgital")

def time():
    string = strftime ("%H:%M:%S")
    Label.config(text=string)
    Label.after(1000, time)

Label = Label (root,font=("ds-digital", 80), background="black", foreground="purple")
Label.pack(anchor="center")
time()

mainloop()