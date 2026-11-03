# create a login interface containing
# 1. A username label and entry field
# 2. A password label and an entry field
# 3. A login button
# Use grid to arrange it neatly

import tkinter as tk
root = tk.Tk()
root.geometry("400x300")

tk.Label(root,text="Username:").grid(row=0,column=0, pady=10)
tk.Entry(root).grid(row=0,column=1)
tk.Label(root,text="Password:").grid(row=2,column=0)
tk.Entry(root).grid(row=2,column=1)
tk.Button(root,text="Login").grid(row=4,column=1, pady=10)
root.mainloop()