import tkinter as tk
root = tk.Tk()
root.title("Scrollable Listbox")
root.geometry("300x250")

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(root, yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=listbox.yview)

for i in range(1,51):
    listbox.insert(tk.END, f"Item{i}")

root.mainloop()

# NOTE:
# yscrollcommand=scrollbar.set : Updates the scrollbar when the listbox scrolls.
# scrollbar.config(command=listbox.yview) : allows the scrollbar to control the listbox's vertical scrolling.
# fill=tk.BOTH : allows the Listbox to expand horizontally and vertically.
# expand=True : allows the Listbox to occupy available space.
