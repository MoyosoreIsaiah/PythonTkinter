# What is tkinter? 
# Tkinter is a standard python library used to create GUI(Graphical User Interface), desktop applications
# Key components of tkinter
# * Window(TK): The main application window
# * Label(Label1): Displays texts or images
# * Button(Button1): A clickable button that triggers an actions
# * Entry(Entry1): Accept single user input
# * Text(Text1): Accepts multiline user input
# * Frame(Frame1): A container to organise widgets
# First tkinter program
import tkinter as tk #This imports the tkinter library
root = tk.Tk() #Creates the main application window
root.title("My first app") #Sets the window title
root.geometry("700x600") #The size of the window
root.mainloop() #Starts the tkinter events loop allowing the window to be displayed


