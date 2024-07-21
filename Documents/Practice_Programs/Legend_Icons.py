from tkinter import *
from tkinter import ttk
import math

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
        case "7":
            points = (coordinates[0],coordinates[1]-60,coordinates[0]+52,coordinates[1]+30,coordinates[0]-52,coordinates[1]+30)
            triangle = canvas.create_polygon(points, outline = "red", fill = "yellow", width = 8)
        case "8":
            inner_circle = (coordinates[0]-60,coordinates[1]+60,coordinates[0]+60,coordinates[1]-60)
            points = (coordinates[0],coordinates[1]-60,coordinates[0]+52,coordinates[1]+30,coordinates[0]-52,coordinates[1]+30)
            oval = canvas.create_oval(inner_circle, outline = "blue", fill="white", width = 8)
            triangle = canvas.create_polygon(points, outline = "blue", fill = "blue", width = 8)
        case "9":
            inner_circle = (coordinates[0]-60,coordinates[1]+60,coordinates[0]+60,coordinates[1]-60)
            stemPoints = (coordinates[0],coordinates[1],coordinates[0],coordinates[1]+150)
            octagonPoints = (coordinates[0]-41.5,coordinates[1]+100, coordinates[0]+41.5,coordinates[1]+100,coordinates[0]+100,coordinates[1]+41.5,coordinates[0]+100,coordinates[1]-41.5, coordinates[0]+41.5,coordinates[1]-100, coordinates[0]-41.5,coordinates[1]-100,coordinates[0]-100,coordinates[1]-41.5,coordinates[0]-100,coordinates[1]+41.5)
            octagon = canvas.create_polygon(octagonPoints, outline = "black", fill = "white", width = 8)
            inner_circle = canvas.create_oval(inner_circle, outline = "black", fill = "black", width = 8)
            stem = canvas.create_line(stemPoints, fill = "black", width = 20)
        case "10":
            leftTriPoints = (coordinates[0],coordinates[1], coordinates[0]-100, coordinates[1]-57.75, coordinates[0]-100, coordinates[1]+57.5)
            rightTriPoints = (coordinates[0],coordinates[1], coordinates[0]+100, coordinates[1]-57.75, coordinates[0]+100, coordinates[1]+57.5)
            leftTriangle = canvas.create_polygon(leftTriPoints, outline = "red", fill = "yellow", width = 8)
            rightTriangle = canvas.create_polygon(rightTriPoints, outline = "red", fill = "yellow", width = 8)
        case "11":
            #There is a much much better method for doing this. Implement it in the future. 
            Points = (coordinates[0]-100,coordinates[1]+75,coordinates[0]-75,coordinates[1]+100, coordinates[0]+75,coordinates[1]+100, coordinates[0]+100,coordinates[1]+75, coordinates[0]+100,coordinates[1]-75, coordinates[0]+75,coordinates[1]-100, coordinates[0]-75,coordinates[1]-100,coordinates[0]-100,coordinates[1]-75)
            tLaP = (Points[12]-25,Points[13],Points[14]+50,Points[15]+25)
            tRaP = (Points[8],Points[9]+25,Points[10]-25,Points[11])
            bLaP = (Points[0],Points[1]-25,Points[2]+25,Points[3])
            bRaP = (Points[4]-25,Points[5],Points[6],Points[7]-25)
            vertRectP = (Points[12],Points[13],Points[4],Points[5])
            horzRectP = (Points[14],Points[15],Points[6],Points[7])
            vertRect = canvas.create_rectangle(vertRectP, outline = "black", fill="black")
            horzRect = canvas.create_rectangle(horzRectP, outline = "black", fill="black")
            tLa = canvas.create_arc(tLaP, start = 90, extent = 90, outline = "black", fill="black")
            tRa = canvas.create_arc(tRaP, start = 0, extent= 90, outline = "black", fill="black")
            bLa = canvas.create_arc(bLaP, start = 180, extent= 90, outline = "black", fill="black")
            bRa = canvas.create_arc(bRaP, start = 270, extent= 90, outline = "black", fill="black")
        case "12":
            Points = (coordinates[0]-50,coordinates[1]+86.6,coordinates[0]+50,coordinates[1]+86.6,coordinates[0]+100,coordinates[1],coordinates[0]+50,coordinates[1]-86.6,coordinates[0]-50,coordinates[1]-86.6,coordinates[0]-100,coordinates[1])
            horzLineP = (Points[4],Points[5],Points[10],Points[11])
            vertLineP1 = (Points[0],Points[1],Points[6],Points[7])
            vertLineP2 = (Points[2],Points[3],Points[8],Points[9])
            canvas.create_polygon(Points, outline = "blue", fill = "white", width = 4)
            canvas.create_line(horzLineP, fill = "blue",  width = 4)
            canvas.create_line(vertLineP1, fill = "blue",  width = 4)
            canvas.create_line(vertLineP2, fill = "blue",  width = 4)
        case "13":
            inner_circle = (coordinates[0]-60,coordinates[1]+60,coordinates[0]+60,coordinates[1]-60)
            arc = canvas.create_arc(inner_circle, start = 0, extent = 90, fill = "yellow", outline = "red", width = 8)
            arc = canvas.create_arc(inner_circle, start = 90, extent = 90, fill = "red", outline = "red", width = 8)
            arc = canvas.create_arc(inner_circle, start = 180, extent = 90, fill = "yellow", outline = "red", width = 8)
            arc = canvas.create_arc(inner_circle, start = 270, extent = 90, fill = "red", outline = "red", width = 8)
        case "14":
            Points = (coordinates[0]-50,coordinates[1]+86.6,coordinates[0]+50,coordinates[1]+86.6,coordinates[0]+100,coordinates[1],coordinates[0]+50,coordinates[1]-86.6,coordinates[0]-50,coordinates[1]-86.6,coordinates[0]-100,coordinates[1])
            triangle1P = (coordinates[0],coordinates[1],Points[0],Points[1],Points[2],Points[3])
            triangle2P = (coordinates[0],coordinates[1],Points[2],Points[3],Points[4],Points[5])
            triangle3P = (coordinates[0],coordinates[1],Points[4],Points[5],Points[6],Points[7])
            triangle4P = (coordinates[0],coordinates[1],Points[6],Points[7],Points[8],Points[9])
            triangle5P = (coordinates[0],coordinates[1],Points[8],Points[9],Points[10],Points[11])
            triangle6P = (coordinates[0],coordinates[1],Points[10],Points[11],Points[0],Points[1])
            traingle1 = canvas.create_polygon(triangle1P, outline = "blue", fill = "white", width = 8)
            traingle2 = canvas.create_polygon(triangle2P, outline = "blue", fill = "blue", width = 8)
            traingle3 = canvas.create_polygon(triangle3P, outline = "blue", fill = "white", width = 8)
            traingle4 = canvas.create_polygon(triangle4P, outline = "blue", fill = "blue", width = 8)
            traingle5 = canvas.create_polygon(triangle5P, outline = "blue", fill = "white", width = 8)
            traingle6 = canvas.create_polygon(triangle6P, outline = "blue", fill = "blue", width = 8)
        case "15":
            bgSquareP = (coordinates[0]-80,coordinates[0]-100,coordinates[0]+100,coordinates[1]+80)
            fgSquareP = (coordinates[0]-100,coordinates[0]-80,coordinates[0]+80,coordinates[1]+100)
            bgSquare = canvas.create_rectangle(bgSquareP, outline = "black", fill="white", width = 8)
            fgSquare = canvas.create_rectangle(fgSquareP, outline = "black", fill="black")
        case "16":
            vertLine1 = (coordinates[0]-50,coordinates[1]-50,coordinates[0]-50,coordinates[1]+50)
            vertLine2 = (coordinates[0],coordinates[1]-75,coordinates[0],coordinates[1]+75)
            vertLine3 = (coordinates[0]+50,coordinates[1]-50,coordinates[0]+50,coordinates[1]+50)
            box = (coordinates[0]-100,coordinates[1]+100,coordinates[0]+100,coordinates[1]-100)
            rect = canvas.create_rectangle(box, outline= "black", fill = "white", width = 8)
            circl = canvas.create_oval(box, outline= "black", fill = "white", width = 8)
            line1 = canvas.create_line(vertLine1, fill = "black", width = 8)
            line2 = canvas.create_line(vertLine2, fill = "black", width = 8)
            line3 = canvas.create_line(vertLine3, fill = "black", width = 8)
        case _:
            ErrHandl = "Error: undefined item"
            print(ErrHandl)
            
def itemReturn():
    canvas.delete("all")
    iconStyle = Combo.get()
    coordinates = 200,200
    iconDiagram(iconStyle, coordinates)

root = Tk()

frame=Frame(root,width=400,height=400)
frame.pack(expand = True, fill=BOTH)

canvas = Canvas(frame, bg='white', width = 400, height=400)

vlist = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","Banana"]

Combo = ttk.Combobox(frame, values = vlist)
Combo.set("Pick an Option")
Combo.pack(padx = 5, pady = 5)

Button = Button(frame, text = "Submit", command = itemReturn)
Button.pack(padx = 5, pady = 5)
canvas.pack(expand = True, fill = BOTH)

root.mainloop()