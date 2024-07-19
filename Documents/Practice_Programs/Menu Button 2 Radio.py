from tkinter import *

root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()

MenuBttn = Menubutton(frame, text = "Favourite food", relief = RAISED)

Var1 = IntVar()

Menu1 = Menu(MenuBttn, tearoff = 0)

Menu1.add_radiobutton(label = "Pizza", variable = Var1, value = 1)
Menu1.add_radiobutton(label = "Cheese Burger", variable = Var1, value = 2)
Menu1.add_radiobutton(label = "Salad", variable = Var1, value = 3)

MenuBttn["menu"] = Menu1

MenuBttn.pack()
root.mainloop()