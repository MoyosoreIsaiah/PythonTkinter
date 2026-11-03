# Class work
# Create a registration form with a submit button that:
# Checks whether the name field is empty
# Displays a warning message if it is empty.
# Displays a confirmation popup if the field contains a name.
# Display a success message if the user confirms the action.


import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x200")


tk.Label(root,text="Username :").grid(row=0,column=0)
entry = tk.Entry(root)
entry.grid(row=0,column=1, pady=10)

tk.Label(root,text="Password :").grid(row=1,column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1,column=1, pady=10)

def register():
    name = entry.get()
    password = entry2.get()
    if not name:
        messagebox.showwarning("warning", "Field must not be empty")
    else:
        answer = messagebox.askyesno("confirm", "Ensure all fields are correct")
        if answer:
            messagebox.showinfo("Success", "Registration Successful")


tk.Button(root, text="Register", command=register).grid(row=2,column=1, pady=10)

root.mainloop()

