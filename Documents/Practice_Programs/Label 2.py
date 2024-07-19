from tkinter import *

def changecolor():
    label.configure(fg = "blue")
    
root = Tk()
button = Button(root, text='Choose Color', command = changecolor).pack(pady=20)
label = Label(root, text = "Color", fg = "black")
label.pack()

root.geometry('180x160')
root.mainloop()