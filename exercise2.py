# class work
# Build a course selection form with the following features:
# 1. A label displaying select your course
# 2. A listbox containing python, java, javascript, and c++
# 3. A combobox containing beginner, intermediate, and advanced
# 4. A submit button that displays the selected course and level
# 5. A clear button that clears the course selection and resets the level
# Note: For the listbox, use curselection() to retrieve the selected course
# For the combobox, use get() to retrieve the selected level.


import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Listbox Widgets")
root.geometry("300x200")

tk.Label(root,text="Select your course:").pack()
listbox = tk.Listbox(root, width=100, height=20)
listbox.pack(pady=10)

listbox.insert(tk.END, "python")
listbox.insert(tk.END, "Java")
listbox.insert(tk.END, "Javascript")
listbox.insert(tk.END, "C++")


combo = ttk.Combobox(root, values = ["beginner", "intermediate", "Advanced"], state="readonly")
combo.pack(pady=20)

def show_selection():
    
    selections = []
    selected = listbox.curselection()
    for i in selected:
        selections.append(listbox.get(i))
        
    if selected:
        
        messagebox.showinfo("Selections:", "\n".join(map(str, selections)))
    else:
        messagebox.showwarning("warning", "Please select an item")
        
    selected2 = combo.get()
    
    if selected2:
        messagebox.showinfo("Selection", selected2)
    else:
        messagebox.showwarning("Warning", "Please select a language")


def clear():
    listbox.select_clear(0, tk.END)
    combo.set("")






tk.Button(root, text="submit", command=show_selection).pack()
tk.Button(root, text="clear", command=clear).pack()


root.mainloop()
