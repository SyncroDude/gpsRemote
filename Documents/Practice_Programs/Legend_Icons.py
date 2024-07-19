from tkinter import *
from tkinter import ttk

def iconDiagram(iconStyle, coordinates):
    match iconStyle:
        case "1":
            outer_circle = (coordinates[0]-100,coordinates[1]+100,coordinates[0]+100,coordinates[1]-100)
            inner_circle = (coordinates[0]-60,coordinates[1]+60,coordinates[0]+60,coordinates[1]-60)
            oval = canvas.create_oval(outer_circle, fill="yellow", width = 8)
            oval = canvas.create_oval(inner_circle, fill="black")
        case "2":
            outer_circle = (coordinates[0]-100,coordinates[1]+100,coordinates[0]+100,coordinates[1]-100)
            oval = canvas.create_oval(outer_circle, fill="yellow", width = 8)
        case "3":
            outer_circle = (coordinates[0]-100,coordinates[1]+100,coordinates[0]+100,coordinates[1]-100)
            arc = canvas.create_arc(outer_circle, start = 0, extent = 180, fill = "yellow", width = 8)
            arc = canvas.create_arc(outer_circle, start = 0, extent = -180, fill = "black", width = 8)
        case "4":
            inner_circle = (coordinates[0]-60,coordinates[1]+60,coordinates[0]+60,coordinates[1]-60)
            oval = canvas.create_oval(inner_circle, fill="yellow", width = 8)
        case "5":
            inner_circle = (coordinates[0]-60,coordinates[1]+60,coordinates[0]+60,coordinates[1]-60)
            arc = canvas.create_arc(inner_circle, start = 0, extent = 180, fill = "yellow", width = 8)
            arc = canvas.create_arc(inner_circle, start = 0, extent = -180, fill = "black", width = 8)
        case "6":
            smaller_circle = (coordinates[0]-40,coordinates[1]+40,coordinates[0]+40,coordinates[1]-40)
            verticalLine = (coordinates[0],coordinates[1]+40,coordinates[0],coordinates[1]-40)
            horizontalLine = (coordinates[0]-40,coordinates[1],coordinates[0]+40,coordinates[1])
            oval = canvas.create_oval(smaller_circle, fill="yellow", width = 6)
            canvas.create_line(verticalLine, fill = "black", width = 6)
            canvas.create_line(horizontalLine, fill = "black", width = 6)
            
            
def itemReturn():
    canvas.delete("all")
    iconStyle = Combo.get()
    coordinates = 200,200
    iconDiagram(iconStyle, coordinates)

root = Tk()

frame=Frame(root,width=400,height=400)
frame.pack(expand = True, fill=BOTH)

canvas = Canvas(frame, bg='white', width = 400, height=400)

vlist = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]

Combo = ttk.Combobox(frame, values = vlist)
Combo.set("Pick an Option")
Combo.pack(padx = 5, pady = 5)

Button = Button(frame, text = "Submit", command = itemReturn)
Button.pack(padx = 5, pady = 5)
canvas.pack(expand = True, fill = BOTH)

root.mainloop()