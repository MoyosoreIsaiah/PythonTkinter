import tkinter as tk

def calc():
    num1 = int(entry.get())
    num2 = int(entry2.get())
    num3 = num1 + num2
    label.config(text=num3)


root = tk.Tk()
root.geometry("400x300")

tk.Label(root, text="Enter the first number").pack(pady=5)
entry = tk.Entry(root)
entry.pack() 

tk.Label(root, text="Enter the second number").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Calculate",command=calc).pack(pady=5)

label = tk.Label(root,text="")
label.pack(pady=5)


root.mainloop()







