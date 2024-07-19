from tkinter import*

root = Tk()

frame=Frame(root,width=300,height=300)
frame.pack(expand = True, fill=BOTH)

canvas = Canvas(frame,bg='white', width = 300, height = 300)

file = PhotoImage(file = "/home/SyncTestBench/Pictures/practice_image.png")
image = canvas.create_image(150, 150, image=file)

canvas.pack(expand = True, fill = BOTH)

root.mainloop()