import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Scrollable_Course_Catalogue")
root.geometry("400x300")

head_frame = tk.Frame(root)
head_frame.pack(side=tk.TOP, fill="x")

main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

left_frame = tk.Frame(main_frame)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

right_frame = tk.Frame(main_frame)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

label = tk.Label(head_frame, text="Course Catalogue", bg="blue", font= ("Times New Roman", 24, "bold"), fg="white", pady=10)
label.pack(fill="x")

courses = [
    "Introduction to Programming", "Data Structures", "Algorithms",
    "Database Systems", "Operating Systems", "Computer Networks",
    "Software Engineering", "Web Development", "Mobile App Development",
    "Artificial Intelligence", "Machine Learning", "Cybersecurity",
    "Computer Architecture", "Discrete Mathematics", "Linear Algebra",
    "Calculus", "Statistics", "Probability Theory",
    "Human-Computer Interaction", "Cloud Computing", "Computer Graphics",
    "Compiler Design", "Information Systems", "Digital Logic Design",
    "Object-Oriented Programming", "Data Mining", "Natural Language Processing",
    "Embedded Systems", "Project Management", "Technical Writing",
]

scrollbar = tk.Scrollbar(left_frame, orient=tk.VERTICAL)

course_list = tk.Listbox(left_frame, height=30, width=50, selectmode=tk.MULTIPLE, yscrollcommand=scrollbar.set)
course_list.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

scrollbar.config(command=course_list.yview)

for course in courses:
    course_list.insert(tk.END, course)


scrollbar2 = tk.Scrollbar(right_frame, orient=tk.VERTICAL)

text_box = tk.Text(right_frame, width=100, yscrollcommand=scrollbar2.set)
text_box.pack(side=tk.LEFT, fill=tk.BOTH)

text_box.insert(tk.END, "Welcome to the Course Catalogue! \n\n")
text_box.insert(tk.END, "Explore our available courses in AI, Data Science, Cloud Computing!, Cyber Security, Software\nDevelopment and Networking. \n\n")
text_box.insert(tk.END, "Enhance your skills.Build your future!")
text_box.config(state="disabled")

text_box.tag_configure("title_head", font=("Times New Roman", 20, "bold"))
text_box.tag_add("title_head", "1.0", "1.end")
scrollbar2.pack(side=tk.LEFT, fill=tk.BOTH)

def show_courses():
    selection = []
    selected = course_list.curselection()

    for i in selected:
        selection.append(course_list.get(i))
    
    if selected:
        messagebox.showinfo("Selected Courses:", "\n".join(map(str, selection)))
    else:
        messagebox.showwarning("Invalid Selection", "Select a course")
        

tk.Button(root, text="Show Selected Courses", bg="blue", font=("Times New Roman", 16, "bold"), fg="white", command=show_courses).pack(pady=10)



root.mainloop()

















