import tkinter as tk
app = tk.Tk()
app.title("Using place")
app.geometry("400x300")
tk.Label(app,text="Welcome").place(x=150,y=50)
tk.Button(app,text="Login").place(x=160,y=100)
app.mainloop()

