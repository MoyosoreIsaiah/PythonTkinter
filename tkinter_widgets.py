# What are widgets?
# Widgets are GUI elements used to build and interact with a tkinter application. In order words, they are building blocks
# Common tkinter widgets:
# * Label(Label1): Displays texts or images
# * Button(Button1): A clickable button that triggers an actions
# * Entry(Entry1): Accept single user input
# * Text(Text1): Accepts multiline user input
# * Frame(Frame1): A container to organise widgets
# * Check Button: A check box that allows users to select or deselect an option
# * Radio Button: Is a button that allows users to select one option from a group of options

import tkinter as tk
root = tk.Tk()
root.title("Tkinter widgets")
root.geometry("400x300")
label = tk.Label(root,text="Enter your name") #Creates a label
label.pack() #Adds label to window
entry = tk.Entry(root) #creates an input field
entry.pack() #Adds the input field to the window
button = tk.Button(root,text="submit") #creates a button
button.pack() #Adds the button to the windows
root.mainloop()




