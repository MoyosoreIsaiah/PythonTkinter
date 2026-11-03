# Practice Exercise

# Create a window with a button labelled Change Text. When clicked
# It should change a label's text to your name.

import tkinter as tk

def name():
    label.config(text="Moyosoreoluwa!") #Update the label text
    

root = tk.Tk()
root.geometry("400x300")

label = tk.Label(root,text="Click the button")
label.pack()

button = tk.Button(root,text="Change Text",command=name)
button.pack()

root.mainloop()