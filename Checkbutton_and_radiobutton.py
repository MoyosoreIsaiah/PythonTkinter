# Checkbutton and Radiobutton Widgets
# 1. Checkbutton: A Checkbutton allows users to select or deselect an option independently.

# 2. Radiobutton: A Radiobutton allows users to select only one option from a group.

# Example: Checkbutton and Radiobutton

import tkinter as tk

root = tk.Tk()
root.title("Selection Form")
root.geometry("350x300")

# checkbutton
subscribe = tk.BooleanVar()

tk.Checkbutton(root, text="Subscribe to newsletter", variable=subscribe).pack(pady=10)

# Radiobutton
gender = tk.StringVar(value="Male")

tk.Radiobutton(root, text="Male",variable=gender,value="Male").pack()

tk.Radiobutton(root, text="Female",variable=gender,value="Female").pack()

# Display Selections

def show_selection():
    print("Subscribed:", subscribe.get())
    print("Gender:", gender.get())

tk.Button(root,text="Submit",command=show_selection).pack(pady=10)

root.mainloop()

# Note:
# text="Male" is the visible text displayed beside the radiobutton in the window.

# variable=gender: Links the Radiobutton to the Tkinter varianle named gender.

# value="Male": The value assigned to gender when this Radiobutton is selected.