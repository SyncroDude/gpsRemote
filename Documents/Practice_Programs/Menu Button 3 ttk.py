from tkinter import *
from tkinter.ttk import *
import tkinter
from ttk import Menubutton

def f():
    var.set("Food")

root = Tk()

var = StringVar()

mb = Menubotton (root, textvariable = var)
mb.pack()
mb.menu = Menu (mb, tearoff = 0 )
mb["menu"] = mb.menu

b = Button(root, text - "Click", command = f)
b.pack()

mayoVar = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton ( label="mayo", variable=mayoVar)
mb.menu.add_checkbutton ( label="ketchup", variable=ketchVar)

mb.pack()
root.mainloop()