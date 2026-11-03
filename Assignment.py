# Assignment
# create a window containing a label displaying your full name, 
# an entry field for entering your age and a button labelled submit.

import tkinter as tk
root = tk.Tk()
root.title("Assesment")
root.geometry("400x300")
label = tk.Label(root,text="Moyosoreoluwa")
label.pack()
label = tk.Label(root,text="Enter your Age") #Creates a label
label.pack() #Adds label to window
entry = tk.Entry(root) #creates an input field
entry.pack() #Adds the input field to the window
button = tk.Button(root,text="submit") #creates a button
button.pack() #Adds the button to the windows
root.mainloop()