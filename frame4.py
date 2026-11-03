# Nested frames
# A frame can contain another frame

#This is called nesting, and it allows you to build more complex  layouts.

#For example, a login form might have:
#A main frame.
# A smaller Frame for the username.
# Another Frame for the password.
# A seperate Frame for the buttons.

import tkinter as tk

root = tk.Tk()
root.title("Nested Frames")
root.geometry("400x300")

main_frame = tk.Frame(root, bg="lightgray", padx=20, pady=20)
main_frame.pack(pady=30)

inner_frame = tk.Frame(main_frame, bg="lightblue", padx=20, pady=20)
inner_frame.pack()

label = tk.Label(inner_frame, text="Inside the Inner Frame", bg="lightblue")
label.pack()

root.mainloop()