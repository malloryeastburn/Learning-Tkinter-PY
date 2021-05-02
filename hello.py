#Import everything from tkinter
from tkinter import *

#needed
root = Tk()

#create a label widget
#2 step process
#1. Define 2. Display
#name_widget = Type_widget(go_where, text = "what?")
myLabel = Label(root, text = "Hello World")

#pack it
myLabel.pack()

#create an event loop
root.mainloop()
