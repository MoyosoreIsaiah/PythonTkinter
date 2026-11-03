# placing widgets inside a frame

# This is one of the most importtant things to understand about frames.
# Instead of placing every widgets directly inside the main window, you can place related widgets inside a frame.

import tkinter as tk
app = tk.Tk()
app.title("widgets inside a frame")
app.geometry("400x300")
app.config(bg="hotpink")

frame = tk.Frame(app, bg="lightblue", width=500, height=500, padx=20, pady=20)
frame.pack(pady=30)
frame.pack_propagate(False)

label = tk.Label(frame, text="Welcome to Tkinter")
label.pack()

button = tk.Button(frame, text="Click Me")
button.pack(pady=10)


app.mainloop()