from tkinter import *

root = Tk()

frame=Frame(root,width=300,height=300)
frame.pack(expand = True, fill=BOTH)

canvas = Canvas(frame, bg="white", width = 300,height = 300)

coordinates = 150, 150
outer_circle = (coordinates[0]-100,coordinates[1]+100,coordinates[0]+100,coordinates[1]-100)
inner_circle = (coordinates[0]-60,coordinates[1]+60,coordinates[0]+60,coordinates[1]-60)
#arc = canvas.create_arc(coordinates, start=0, extent=250, fill="blue")
#arc = canvas.create_arc(coordinates, start=250, extent=50, fill="red")
#arc = canvas.create_arc(coordinates, start=300, extent=60, fill="yellow")

oval = canvas.create_oval(outer_circle, fill="yellow", width = 8)
oval = canvas.create_oval(inner_circle, fill="black")

canvas.pack(expand = True, fill = BOTH)

root.mainloop()