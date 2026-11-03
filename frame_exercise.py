# Title: Login System
# Dimensions: 400x350
# Header Frame
# Background color: dark blue
# contains a label displaying User Login
# The label's text colour must be white.
# Form Frame
# contains a label displaying username.
# contains a entry widget for the username
# contains a label displaying password
# contains a entry widget for the password.
# The password entry must hide typed characters using show="*".
# Button Frame
# contains a Login Button
# contains a clear button.
# Additional requirements
# use these seperate frames.
# place each widget inside the appropriate frame.
# use padding to improve the layout.
# the clear button must clear both entry widgets.
# the Login button must display an informational message using messagebox.showinfo()



import tkinter as tk
root = tk.Tk()
root.title("Login System")
root.geometry("400x350")

header = tk.Frame(root, bg="darkblue", padx=20, pady=20)
header.pack(fill="x")

label = tk.Label(header, text="User Login", bg="darkblue", fg="white")
label.pack(pady=20)


form = tk.Frame(root, bg="lightgrey", padx=50, pady=50)
form.pack(fill="both", expand=True)

label2 = tk.Label(form, text="Username")
label2.pack(pady=10)

entry = tk.Entry(form)
entry.pack(pady=10)

label3 = tk.Label(form, text="Password")
label3.pack(pady=20)

entry2 = tk.Entry(form)
entry2.pack(pady=10)

button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(fill="x")

button1 = tk.Button(button_frame, text="click me")
button1.pack(pady=10)

# def clear():


root.mainloop()











