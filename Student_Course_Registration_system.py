import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Student Course Registration System")
root.geometry("600x650")
root.resizable(False, False)
root.configure(bg="black")


# Store the submitted registration
registration_data = None


#TKINTER VARIABLES

full_name_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()

terms_var = tk.BooleanVar()
learning_mode_var = tk.StringVar(value="")
experience_var = tk.StringVar(value="")


# HEADER 

header_frame = tk.Frame(root, bg="black", height=45)
header_frame.pack(fill="x", padx=10, pady=5)
header_frame.pack_propagate(False)

title_label = tk.Label(
    header_frame,
    text="STUDENT COURSE REGISTRATION",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="black"
)
title_label.place(relx=0.5, rely=0.5, anchor="center")


#FORM FRAME

form_frame = tk.Frame(root, bg="black")
form_frame.pack(fill="both", expand=True, padx=15, pady=3)

# form_frame.columnconfigure(1, weight=1)



# Personal details
tk.Label(
    form_frame, text="Full Name:", bg="black", fg="white"
).grid(row=0, column=0, sticky="w", padx=5, pady=3)

name_entry = tk.Entry(
    form_frame, textvariable=full_name_var, width=35
)
name_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=3)


tk.Label(
    form_frame, text="Email Address:", bg="black", fg="white"
).grid(row=1, column=0, sticky="w", padx=5, pady=3)

email_entry = tk.Entry(
    form_frame, textvariable=email_var
)
email_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=3)


tk.Label(
    form_frame, text="Phone Number:", bg="black", fg="white"
).grid(row=2, column=0, sticky="w", padx=5, pady=3)

phone_entry = tk.Entry(
    form_frame, textvariable=phone_var
)
phone_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=3)


# Additional information
tk.Label(
    form_frame,
    text="About Yourself / Your Goals:",
    bg="black", fg="white"
).grid(row=3, column=0, columnspan=2, sticky="w",
       padx=5, pady=5)

about_text = tk.Text(form_frame, height=3, width=55)
about_text.grid(row=4, column=0, columnspan=2,
                sticky="ew", padx=5, pady=3)


# Learning mode
tk.Label(
    form_frame, text="Learning Mode:", bg="black", fg="white"
).grid(row=5, column=0, sticky="w", padx=5, pady=3)

mode_frame = tk.Frame(form_frame, bg="black")
mode_frame.grid(row=5, column=1, sticky="w", padx=5)

for mode in ["Physical", "Online", "Hybrid"]:
    tk.Radiobutton(
        mode_frame,
        text=mode,
        variable=learning_mode_var,
        value=mode,
        bg="black", fg="white"
    ).pack(side="left", padx=3)


# Course selection
tk.Label(
    form_frame, text="Select Courses:", bg="black", fg="white"
).grid(row=6, column=0, sticky="nw", padx=5, pady=4)

course_frame = tk.Frame(form_frame, bg="black")
course_frame.grid(row=6, column=1, sticky="ew", padx=5, pady=3)

course_list = tk.Listbox(
    course_frame,
    selectmode=tk.MULTIPLE,
    height=5,
    exportselection=False
)

courses = [
    "Python Programming",
    "Java Programming",
    "Web Development", 
    "Database Management",
    "Data Analysis",
    "Mobile App Development"
]

for course in courses:
    course_list.insert(tk.END, course)

course_list.pack(side="left", fill="x", expand=True)

course_scrollbar = tk.Scrollbar(
    course_frame, command=course_list.yview
)
course_scrollbar.pack(side="right", fill="y")
course_list.config(yscrollcommand=course_scrollbar.set)


def clear_courses():
    course_list.selection_clear(0, tk.END)


tk.Button(
    form_frame,
    text="Clear Course Selection",
    command=clear_courses
).grid(row=7, column=1, sticky="w", padx=5, pady=2)


# Experience level
tk.Label(
    form_frame, text="Experience Level:", bg="black", fg="white"
).grid(row=8, column=0, sticky="w", padx=5, pady=3)

experience_box = ttk.Combobox(
    form_frame,
    textvariable=experience_var,
    values=["Beginner", "Intermediate", "Advanced"],
    state="readonly",
    width=25
)
experience_box.grid(row=8, column=1, sticky="w", padx=5, pady=3)


def clear_experience():
    experience_box.set("")


tk.Button(
    form_frame,
    text="Clear Experience",
    command=clear_experience
).grid(row=9, column=1, sticky="w", padx=5, pady=2)


# Terms and conditions
terms_check = tk.Checkbutton(
    form_frame,
    text="I agree to the registration terms and conditions.",
    variable=terms_var,
    fg="white", bg="black"
)
terms_check.grid(
    row=10, column=0, columnspan=2,
    sticky="w", padx=5, pady=5
)
tk.Radiobutton

#REGISTER FUNCTION

def register_student():
    global registration_data

    try:
        name = full_name_var.get().strip()
        email = email_var.get().strip()
        phone = phone_var.get().strip()
        about = about_text.get("1.0", "end-1c").strip()

        selected_indices = course_list.curselection()
        selected_courses = [
            course_list.get(index)
            for index in selected_indices
        ]

        experience = experience_box.get().strip()
        learning_mode = learning_mode_var.get().strip()

        # Validate required fields
        if not name or not email or not phone:
            messagebox.showwarning(
                "Missing Information",
                "Please enter your full name, email and phone number."
            )
            return

        if not selected_courses:
            messagebox.showwarning(
                "Course Required",
                "Please select at least one course."
            )
            return

        if not experience:
            messagebox.showwarning(
                "Experience Required",
                "Please select your experience level."
            )
            return

        if not learning_mode:
            messagebox.showwarning(
                "Learning Mode Required",
                "Please select your preferred learning mode."
            )
            return 

        if not terms_var.get():
            messagebox.showwarning(
                "Terms and Conditions",
                "You must agree to the terms and conditions."
            )
            return

        # Save the submitted information
        registration_data = {
            "Full Name": name,
            "Email Address": email,
            "Phone Number": phone,
            "Additional Information": about or "None provided",
            "Selected Courses": selected_courses,
            "Experience Level": experience,
            "Learning Mode": learning_mode,
            "Terms Accepted": "Yes"
        }

        messagebox.showinfo(
            "Registration Successful",
            f"Registration completed successfully!\nWelcome, {name}."
        )

    except Exception as error:
        messagebox.showerror(
            "Registration Error",
            f"An error occurred:\n{error}"
        )


#VIEW REGISTRATION

def view_registration():
    if registration_data is None:
        messagebox.showwarning(
            "No Registration",
            "Please register a student before viewing details."
        )
        return

    # Bonus: create a separate window
    details_window = tk.Toplevel(root)
    details_window.title("Registration Details")
    details_window.geometry("450x450")
    details_window.configure(bg="navyblue")
    details_window.resizable(False, False)

    tk.Label(
        details_window,
        text="SUBMITTED REGISTRATION DETAILS",
        font=("Arial", 12, "bold"),
        bg="navyblue"
    ).pack(pady=10)

    details_text = tk.Text(
        details_window, height=20, width=48, wrap="word"
    )
    details_text.pack(padx=10, pady=5, fill="both", expand=True)

    for key, value in registration_data.items():
        if isinstance(value, list):
            value = ", ".join(value)

        details_text.insert(
            tk.END, f"{key}: {value}\n\n"
        )

    details_text.config(state="disabled")


# CLEAR FORM

def clear_form():
    answer = messagebox.askyesno(
        "Confirm Clear",
        "Are you sure you want to clear the form?"
    )

    if answer:
        full_name_var.set("")
        email_var.set("")
        phone_var.set("")

        about_text.delete("1.0", tk.END)
        clear_courses()
        clear_experience()

        terms_var.set(False)
        learning_mode_var.set("")

        messagebox.showinfo(
            "Form Cleared",
            "All form fields have been cleared."
        )


# BUTTONS

button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=8)

tk.Button(
    button_frame,
    text="Register",
    command=register_student,
    width=12,
    bg="black",
    fg="white"
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="View Registration",
    command=view_registration,
    width=16
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Clear Form",
    command=clear_form,
    width=12
).grid(row=0, column=2, padx=5)



root.mainloop()