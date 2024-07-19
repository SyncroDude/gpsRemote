from tkinter import *

root = Tk()

frame=Frame(root,width=300,height=300)
frame.pack(expand = True, fill=BOTH)

canvas = Canvas(frame, bg='white', width = 300, height=300)

coordinates = 50, 50, 250, 250
arc = canvas.create_line(coordinates, fill="blue")

coordinates = 250, 50, 50, 250
arc = canvas.create_line(coordinates, fill="red")

canvas.pack(expand = True, fill = BOTH)

root.mainloop()