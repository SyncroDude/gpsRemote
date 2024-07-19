from tkinter import *

def retrieve():
    print(Var1.get())
    print(Var2.get())

root = Tk()
root.geometry("200x150")

frame = Frame(root)
frame.pack()

Var1 = IntVar()
Var2 = IntVar()

ChkBttn = Checkbutton(frame, text = "Option1", variable = Var1)
ChkBttn.pack(padx = 5, pady = 5)

ChkBttn2 = Checkbutton(frame, text = "Option2", variable = Var2)
ChkBttn2.pack(padx = 5, pady = 5)

Button = Button(frame, text = "Submit", command = retrieve)
Button.pack(padx = 5, pady = 5)

#You can also use the command = retrieve right in the checkbox item, however it will update everytime the box is checked/unchecked, which may cause issues.

root.mainloop()