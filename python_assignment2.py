# Assignment 2: Simle Calculator

# Create a window titled 'simple calculator'.
# provide two 'entry' fields for numerical input.
# Add an 'Add numbers' button.
# When clicked, retrieve both values, convert them to numbers, and display their sum in a label.
# use 'grid()' and padding to organize the interface.
# display an error message if either field is empty.
# prevent program from crashing when a user enters letters instead of numbers. Display 'invalid input!' instead.

# 2.
import tkinter as tk
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("500x400")

def calc():
    class numbercannotbeempty(Exception):
        pass
    
    try:
        num1 = int(entry.get())
        num2 = int(entry2.get())
        add = num1 + num2
        label.config(text=f"{num1},{num2}")
        label2.config(text=add)

        if not num1 and not num2:
            raise numbercannotbeempty("cannot be empty")
    
            return
    except ValueError:
        print("Error: Invalid Input, must be a number")
    try:

    except numbercannotbeempty as e:
        print("Error:", e)
    

tk.Label(root, text="Enter first number").grid(row=0,column=0)
entry = tk.Entry(root)
entry.grid(row=0,column=1)

tk.Label(root, text="Enter second number").grid(row=1,column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1,column=1)

tk.Button(root,text="Add numbers",command=calc).grid(row=2,column=1, pady=5)


label = tk.Label(root,text="")
label.grid(row=3,column=1)

label2 = tk.Label(root,text="")
label2.grid(row=4,column=1)

root.mainloop()









