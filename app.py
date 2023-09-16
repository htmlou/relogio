from tkinter import *
from tkinter import *

from time import strftime

root = Tk ()
root.tittle("Relógio DIgital")

def time():
    string = strftime ("%H:%M:%S")
    Label.config(text=string)
    Label.after(1000, time)
