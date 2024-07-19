import tkinter as tk


class Window:
    def __init__(self, master):
        self.master = master
        
        self.frame = tk.Frame(self.master)
        self.frame.pack
        
        self.scrollbary = tk.Scrollbar(self.frame, orient = tk.VERTICAL)
        self.scrollbary.pack(side = tk.RIGHT, fill = tk.Y)
        self.scrollbarx = tk.Scrollbar(self.frame, orient = tk.HORIZONTAL)
        self.scrollbarx.pack(side = tk.BOTTOM, fill = tk.X)
        
        self.canvas = tk.Canvas(self.frame, width = 300, height = 300, bg = "white", scrollregion = (0,0,500,500), yscrollcommand = self.scrollbary.set, xscrollcommand = self.scrollbarx.set)
        self.canvas.pack()
        
        self.scrollbary.config(command = self.canvas.yview)
        self.scrollbarx.config(command = self.canvas.xview)
        
        img = tk.PhotoImage(file = "/home/SyncTestBench/Pictures/practice_image.png")
        self.master.img = img
        self.canvas.create_image(200,200, image = img)

    
root = tk.Tk()
window = Window(root)
root.mainloop()