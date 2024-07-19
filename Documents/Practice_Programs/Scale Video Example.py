import tkinter as tk

class Window:
    def __init__(self, master):
        self.master = root
        
        # Frame
        self.frame = tk.Frame(self.master, width = 300, height = 200)
        self.frame.pack()
        
        # Scale
        self.scale = tk.Scale(self.frame, from_ = 0, to = 10, orient = tk.HORIZONTAL, command = self.ret, resolution = 1, digit = 2, tickinterval = 1, length = 200, sliderlength = 20, label = "My Scale", showvalue = 0, troughcolor = "blue")
        self.scale.place(x = 30, y=30)
        
        # Button
        self.button = tk.Button(self.frame, text = "DISABLE the Scale", command = self.disable)
        self.button.place(x = 30, y = 100)
        
    def disable(self):
        self.scale.config(state = tk.DISABLED, troughcolor = "grey")
        
    def ret(self, value):
        print(value)

root = tk.Tk()
window = Window(root)
root.mainloop()