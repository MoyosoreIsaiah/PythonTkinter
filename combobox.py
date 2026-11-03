# combobox widget
# A combobox displays a dropdown list from which users can select an option.

# it is provided  by tkinter.ttk, so you must import ttk
import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("combobox widget")
root.geometry("300x200")

combo = ttk.Combobox(root, values = ["python", "Java", "Javascript", "C++"], state="readonly")
combo.pack(pady=20)

# Additional methods

# combo.get() -- Retrieves the selected value
# combo.set("Python") -- Sets the displayed value

# Retrieving a combobox 

def show_selection():
    selected = combo.get()

    if selected:
        messagebox.showinfo("Selection", selected)
    else:
        messagebox.showwarning("Warning", "Please select a language")

def clear():
    combo.set("")

tk.Button(root, text="Submit", command=show_selection).pack()
tk.Button(root, text="clear", command=clear).pack()

root.mainloop()