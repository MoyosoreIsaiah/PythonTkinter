import tkinter as tk
root = tk.Tk()
root.title("Scrollable Text")
root.geometry("400x300")

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_box = tk.Text(root, yscrollcommand=scrollbar.set)
text_box.insert("1.0", "Adeola said nothing same as Femi but Faruq got it right \n Adeola said nothing same as Femi but Faruq got it right \n Adeola said nothing same as Femi but Faruq got it right \n Adeola said nothing same as Femi but Faruq got it right \n Adeola said nothing same as Femi but Faruq got it right \n Adeola said nothing same as Femi but Faruq got it right \n Adeola said nothing same as Femi but Faruq got it right \n Adeola said nothing same as Femi but Faruq got it right \n Adeola said nothing same as Femi but Faruq got it right \n Adeola said nothing same as Femi but Faruq got it right \n Adeola said nothing same as Femi but Faruq got it right \n Adeola said nothing same as Femi but Faruq got it right \n Adeola said nothing same as Femi but Faruq got it right \n Adeola said nothing same as Femi but Faruq got it right \n Adeola said nothing same as Femi but Faruq got it right")
text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=text_box.yview)

root.mainloop()