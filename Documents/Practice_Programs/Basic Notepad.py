import tkinter as tk


class Window:
    def __init__(self, master):
        self.master = master
        
        self.frame = tk.Frame(self.master)
        self.frame.pack(expand = True, fill = tk.BOTH)
        
        self.label = tk.Label(self.frame, text = "My NotePad")
        self.label.pack()
        
        #Creating ScrollBars
        self.scrolly = tk.Scrollbar(self.frame)
        self.scrolly.pack(side = tk.RIGHT, fill = tk.Y)
        self.scrollx = tk.Scrollbar(self.frame, orient = tk.HORIZONTAL)
        self.scrollx.pack(side = tk.BOTTOM, fill = tk.X)
                
        self.text = tk.Text(self.frame, wrap = tk.NONE, undo = True, yscrollcommand = self.scrolly.set, xscrollcommand = self.scrollx.set)
        self.text.pack(expand = True, fill = tk.BOTH)
        
        self.scrolly.config(command = self.text.yview)
        self.scrollx.config(command = self.text.xview)
        
        self.text.insert("1.0", "This is some Sample Data \nThis is Line 2 of the Sample Data\n")
        
        self.img = tk.PhotoImage (file = "/home/SyncTestBench/Pictures/practice_image.png")
        self.text.image_create("end", image = self.img)
        
        
        

root = tk.Tk()
window = Window(root)
root.mainloop() 