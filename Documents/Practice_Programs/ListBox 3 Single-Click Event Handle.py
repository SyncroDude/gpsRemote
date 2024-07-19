import tkinter as tk

def single_click_handler(event):
    selected_index = listbox.curselection()[0]
    selected_item = listbox.get(selected_index)
    print("Single-clicked on:", selected_item)
    
root = tk.Tk()

listbox = tk.Listbox(root)
listbox.pack()

#Bind the single-click event to the Listbox
listbox.bind("<<ListboxSelect>>", single_click_handler)

#Add some items to the Listbox
for item in ["Item 1", "Item 2", "Item 3"]:
    listbox.insert(tk.END, item)
    
root.mainloop()