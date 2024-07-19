import tkinter as tk

def double_click_handler(event):
    selected_index = listbox.curselection()[0]
    listbox.delete(selected_index)
    print("Removed item at index:", selected_index)
    
root = tk.Tk()

listbox = tk.Listbox(root)
listbox.pack()

#Bind the single-click event to the Listbox
listbox.bind("<Double-Button-1>", double_click_handler)

#Add some items to the Listbox
for item in ["Item 1", "Item 2", "Item 3"]:
    listbox.insert(tk.END, item)
#Future - Set up error handling for when there are no more items on the list
root.mainloop()