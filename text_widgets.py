# The Text widgets is used to accept and display multiple lines of text.
# Unlike Entry, which accepts a single line, Text is suitable for
# descriptions, comments, and messages.

# Creating a text widgets

import tkinter as tk  

root = tk.Tk()
root.title("Text widgets")
root.geometry("400x300")


result_label = tk.Label(root, text="")
text_box = tk.Text(root, height=5, width=30)
text_box.pack(pady=10)

# Retrieving text


def show_text():
    message = text_box.get("1.0", tk.END)
    result_label.config(text=message)

def clear():
    text_box.delete("1.0", tk.END)

tk.Button(root, text="Show text", command=show_text).pack()
tk.Button(root, text="Clear text", command=clear).pack()

result_label.pack(pady=10)





# Use .get("1.0", tk.END) to retrieve the text entered by the user.
# Understanding get(1.0, tk.END)
# -"1.0" - Starts at line 1, character position 0.
# - tk.END - specifies the end of the text.
# - .get() - retrieves the text beetween those positions.

# Inserting text
# Use.insert() to add text to the widgets.
# text_box.insert("1.0", "Enter your message here")

# This case, "1.0" specifies when the text should be inserted.

# Clearing the text widgets
# Use .delete("1.0", tk.END) to remove all text.


root.mainloop()

# class work
# Build a Feedback Form with the following features:
# 1. A label displaying "Enter your Feedback".
# 2. A text widgets for multiline inputs.
# 3. A submit button that displays the submitted feedback in a label.
# 4. A clear button that removes all text from the text widgets.


import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Feedback Form")
root.geometry("400x300")


tk.Label(root,text="Enter your Feedback").grid(row=0,column=0)
result_label = tk.Label(root, text="")
text_box = tk.Text(root, height=5, width=30)
text_box.grid(row=1,column=0, pady=10)


def submit():
    message = text_box.get("1.0", tk.END).strip()
    if not message:
        messagebox.showwarning("Error", "The text area cannot be empty")
    else:
        result_label.config(text=message)

def clear():
    answer = messagebox.askyesno("confirm", "Do you want to clear the text?")
    if answer:
        messagebox.showinfo("Success", "Messages cleared successfully")
        text_box.delete("1.0", tk.END) 

tk.Button(root, text="Submit", command=submit).grid(row=2,column=0)
tk.Button(root, text="Clear text", command=clear).grid(row=2,column=1)

result_label.grid(row=3,column=0)

root.mainloop()



