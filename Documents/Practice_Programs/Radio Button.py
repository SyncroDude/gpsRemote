from tkinter import *

def retrieve():
    print(Var1.get())

root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()

Var1 = StringVar()

Rbttn = Radiobutton(frame, text = "Burger", variable = Var1, value = 1)
Rbttn.pack(padx = 5, pady = 5)

RBttn2 = Radiobutton(frame, text = "Pizza", variable = Var1, value = 2)
RBttn2.pack(padx = 5, pady = 5)

Button = Button(frame, text = "Submit", command = retrieve)
Button.pack()
#command - retrieve can also be packed into the radiobutton function, but will return when an input is received.

root.mainloop()