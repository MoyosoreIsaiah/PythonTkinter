# Messagebox Alerts and Notifications
# What is messagebox?
#  A messagebox displays popup dialogs for messages, warning, errors, and confirmations.

# Common Messagebox Methods

# showinfo() - Displays an information message.
# showwarning() - Displays a warning message.
# showerror() - Displays an error message.
# askyesno() - Asks a Yes/No question and returns True or False.



import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x200")

def show_message():
    messagebox.showinfo("Success", "Registration Successful")

def confirm_action():
    answer = messagebox.askyesno("confirm", "Do you want to continue?")
    if answer:
        messagebox.showinfo("Response", "You selected Yes")

tk.Button(root, text="register", command=show_message).pack(pady=10)
tk.Button(root, text="Continue", command=confirm_action).pack(pady=10)

root.mainloop()

