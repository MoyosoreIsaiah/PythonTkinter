# What is Entry?

# Entry is a Tkinter widget used to accept
# single-line text input from users.

# Common Entry Methods

# get(): Retrieves the entered text
# delete(): Removes text from the entry field.
# insert(): Inserts text into  the entry field.

# Example: Retrieving user input
import tkinter as tk
def greet():
    name = entry.get() # Retrieves the entered name
    label.config(text=f"Welcome, {name}!") # Display the name

root = tk.Tk()
root.geometry("400x250")

tk.Label(root, text="Enter your name:").pack(pady=5)

entry = tk.Entry(root) #Create an Input field
entry.pack(pady=5)

tk.Button(root, text="submit",command=greet).pack(pady=5)

label = tk.Label(root,text="")
label.pack(pady=5)

root.mainloop()