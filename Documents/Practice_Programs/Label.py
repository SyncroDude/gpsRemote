from tkinter import *

def set():
    var.set("Good-Bye Cruel World")
    
root = Tk()
root.geometry("200x150")

frame = Frame(root)
frame.pack()

var = StringVar()
var.set("Hello World")

label = Label(frame, textvariable = var )
label.pack()
button = Button(frame, text = "set", command = set)
button.pack()

root.mainloop()