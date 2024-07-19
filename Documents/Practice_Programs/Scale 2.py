from tkinter import *

def val(value):
    print(value)
    
root = Tk()
root.geometry("200x200")
frame = Frame(root)
frame.pack()

Scala = Scale(frame, from_=0, to=10, command=val)
Scala.pack(padx=5, pady=5)

Scala2 = Scale(frame, from_=0, to=10, resolution = 0.5, command=val, orient=HORIZONTAL)
Scala2.pack(padx=5, pady=5)

root.mainloop()