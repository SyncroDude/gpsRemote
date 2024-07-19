import tkinter as tk
from tkinter import ttk

class Window:
    def __init__(self, master):
        self.master = master
        
        # Frame
        self.frame = tk.Frame(self.master, width = 200, height = 200)
        self.frame.pack()
        
        self.vlist = ["Option1", "Option2", "Option3", "Option4", "Option5"]
        
        self.combo = ttk.Combobox(self.frame, values = self.vlist, state = "readonly")
        self.combo.set("Pick an Option")
        self.combo.place(x = 20, y = 50)
        
root = tk.Tk()
root.title("Tkinter")

window = Window(root)
root.mainloop()