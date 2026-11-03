# Assignment 1: Student Registration Form

# Create a window titled 'student Registration System' with dimensions '500x400'.
# Include input fields for Full Name, Age, Email Address and Department.
# Add a 'register' button.
# use 'grid()' to arrange the widgets neatly and apply appropriate padding.
# when the button is clicked, display the student's details in a label below the form.
# If the name field is empty, display 'please enter your name!' instead of registering the student.


# 1.
import tkinter as tk
root = tk.Tk()
root.title("Student Registration System")
root.geometry("500x400")

def info():
    Full_name = str(entry.get())
    Age = int(entry2.get())
    Email_address = str(entry3.get())
    Department = str(entry4.get())
    label.config(text=Full_name)
    label2.config(text=Age)
    label3.config(text=Email_address)
    label4.config(text=Department)



tk.Label(root, text="Enter full name").grid(row=0,column=0)
entry = tk.Entry(root)
entry.grid(row=0,column=1)

tk.Label(root, text="Enter your age").grid(row=1,column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1,column=1)

tk.Label(root, text="Enter you email address").grid(row=2,column=0)
entry3 = tk.Entry(root)
entry3.grid(row=2,column=1)

tk.Label(root,text="Enter your department").grid(row=3,column=0)
entry4 = tk.Entry(root)
entry4.grid(row=3,column=1)

tk.Button(root,text="Register",command=info).grid(row=4,column=1, pady=5)


label = tk.Label(root,text="")
label.grid(row=5,column=1)

label2 = tk.Label(root,text="")
label2.grid(row=6,column=1)

label3 = tk.Label(root,text="")
label3.grid(row=7,column=1)

label4 = tk.Label(root,text="")
label4.grid(row=8,column=1)


root.mainloop()
