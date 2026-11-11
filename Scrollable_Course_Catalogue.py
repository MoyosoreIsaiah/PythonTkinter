# class work: Scrollable Course Catalogue

# Build a desktop application with the following requirements:
# 1. Create a main window with a title and appropriate dimentions.
# 2. Create a Listbox containing at least 30 course names.
# 3. Add a vertical scrollbar to the Listbox.
# 4. Add a Text widgets containing a short description of the courses.
# 5. Add a vertical scrollbar to the text widget.
# 6. Add a button that displays the selected course using a messagebox.


import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Scrollable_Course_Catalogue.py")
root.geometry("400x200")

header_frame = tk.Frame(root, bg="royalblue", height=45)
header_frame.pack(fill="x", padx=10, pady=5)
header_frame.pack_propagate(False)

title_label = tk.Label(
    header_frame,
    text="Course Catalogue",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="royalblue"
)
title_label.place(relx=0.5, rely=0.5, anchor="center")


form_frame = tk.Frame(root, bg="black")
form_frame.pack(fill="both", expand=True, padx=15, pady=3)
# frame1 = tk.Frame(root, bg="grey", width=550, height=500)
# frame1.grid(row=1, column=0, pady=20)

# frame1.pack_propagate(False)
# frame.pack(fill="x", pady=20)
# frame.pack_propagate(False)

# scrollbar = tk.Scrollbar(frame1)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# listbox = tk.Listbox(frame1, yscrollcommand=scrollbar.set, height=20, selectmode=tk.MULTIPLE)
# listbox.pack(pady=10,side=tk.LEFT, expand=True)

# scrollbar.config(command=listbox.yview)

# listbox.insert(tk.END, "python")
# listbox.insert(tk.END, "Java")
# listbox.insert(tk.END, "Javascript")
# listbox.insert(tk.END, "C++")
# listbox.insert(tk.END, "C Programming")
# listbox.insert(tk.END, "C#")
# listbox.insert(tk.END, "PHP")
# listbox.insert(tk.END, "Ruby")
# listbox.insert(tk.END, "Swift")
# listbox.insert(tk.END, "HTML")
# listbox.insert(tk.END, "CSS")
# listbox.insert(tk.END, "React.js")
# listbox.insert(tk.END, "Node.js")
# listbox.insert(tk.END, "Angular")
# listbox.insert(tk.END, "Vue.js")
# listbox.insert(tk.END, "Next.js")
# listbox.insert(tk.END, "Django")
# listbox.insert(tk.END, "Laravel")
# listbox.insert(tk.END, "SQL")
# listbox.insert(tk.END, "Golang")
# listbox.insert(tk.END, "PostgreSQL")
# listbox.insert(tk.END, "MySQL")
# listbox.insert(tk.END, "PostgreSQL")
# listbox.insert(tk.END, "MongoDB")
# listbox.insert(tk.END, "Firebase")
# listbox.insert(tk.END, "Software Engineering")
# listbox.insert(tk.END, "Mobile App Development")
# listbox.insert(tk.END, "Artificial Intelligence")
# listbox.insert(tk.END, "Machine Learning")
# listbox.insert(tk.END, "Cy")

# frame2 = tk.Frame(root, bg="grey", width=550, height=500)
# frame2.grid(row=1, column=1, pady=20)

# scrollbar2 = tk.Scrollbar(frame2)
# scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)

# text_box = tk.Text(frame2, yscrollcommand=scrollbar2.set)
# text_box.insert("1.0", "Explore the world of technology through practical courses designed to build digital skills, logical thinking and problem solving abilities. \n Learn programming languages and tools such as python, java, sql, while gaining knowledge in software development, database management, web development, and other essential areas of technology. \n Whether you're a beginner or looking to improve your skills, there's something to help you grow in the tech industry.")
# text_box.pack(side=tk.Lbersecurity")
# listbox.insert(tk.END, "Cloud ComputingEFT, expand=True)

# scrollbar2.config(command=text_box.yview)


# def show_selected_courses():
#     selections = []
#     selected = listbox.curselection()
#     for i in selected:
#         selections.append(listbox.get(i))
#     if selected:
#         # item = listbox.get(selected)
#         messagebox.showinfo("Selections:", "\n".join(map(str, selections)))
#     else:
#         messagebox.showwarning("warning", "Please select an item")


# tk.Button(root, text="show_selected_courses", command=show_selected_courses).pack()

root.mainloop()