# A frame is a container used to group and organize widgets inside a window.
# Think of a frame as a box inside your application window. You can place labels,
# buttons, entry fields, and other widgets inside that box.

# For example when creating a login form, you can put the username field, and login 
# button inside one frame.



# For instance, you can use seperate frames for a login form,
# navigation buttons, and a registration form.


# Why do we use frames?

# To organize widgets into seperate sections.
# To create cleaner application layouts.
# To manage groups of widgets independently.
# To make complex interfaces easier to structure.


# creating a frame
import tkinter as tk

root = tk.Tk()
root.title("Frame widgets")
root.geometry("400x300")

frame = tk.Frame(root, bg="lightblue", width=550, height=750)
frame.pack(pady=20)

# frame.pack_propagate(False)

root.mainloop()











