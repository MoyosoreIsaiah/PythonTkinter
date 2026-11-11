# Tkinter scrollbar widgets
# A scrollbar is a tkinter widget that allows users to navigate through the content 
# That is too large to fit inside the visible area of another wi

import tkinter as tk
root = tk.Tk()
root.title("Scrollbar Widgets")
root.geometry("400x300")

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

root.mainloop()
