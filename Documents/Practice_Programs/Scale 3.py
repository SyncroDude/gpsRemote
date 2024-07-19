from tkinter import *

def val(value):
    print(value)
    
root = Tk()
root.geometry("200x200")
frame = Frame(root)
frame.pack()

Scala = Scale(frame, from_=0, to=10, command=val)
Scala.pack(padx=5, pady=5)

Scala2 = Scale(frame, from_=0, to=10, length =200, tickinterval = 1, command=val, orient=HORIZONTAL, sliderlength=15)
Scala2.pack(padx=5,pady=5)

root.mainloop()