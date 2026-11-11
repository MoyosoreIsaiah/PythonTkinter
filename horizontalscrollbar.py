# A Horizontal scrollbar allows users to move through content from left to right.


import tkinter as tk

root = tk.Tk()
root.geometry("400x200")

scrollbar = tk.Scrollbar(root, orient = tk.HORIZONTAL)
scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

text_box = tk.Text(root, wrap=tk.NONE, xscrollcommand=scrollbar.set)
text_box.pack(fill=tk.BOTH, expand=True)

scrollbar.config(command=text_box.xview)

root.mainloop()

