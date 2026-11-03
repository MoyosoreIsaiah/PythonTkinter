# What is layout Management?

# Layout Management determines how widgets are arranged/positioned 
# inside a tkinter window.

# Types of layout Managers:
# pack(): Arranges widgets in blocks, typically vertically or horizontally.
# grid(): Arranges widgets in rows and columns.
# place(): positins widgets using specific coordinates.


# Example: Using pack()
import tkinter as tk
root = tk.Tk()
root.geometry("400x300")
root.title("Layout Management")
tk.Label(root,text="Welcome").pack()
tk.Button(root, text="Submit").pack()
tk.Entry(root).pack()
root.mainloop()








