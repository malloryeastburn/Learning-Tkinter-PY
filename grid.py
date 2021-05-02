#Purpose: Learning the grid system

#Import everything from tkinter
from tkinter import *

#needed
root = Tk()

#create a label widget
#2 step process
#1. Define 2. Display

#create the things
#name_widget = Type_widget(go_where, text = "what?") then display it in one line
myLabel1 = Label(root, text = "Hello World").grid(row=0, column=0)
myLabel2 = Label(root, text = "My Name Is Mallory Eastburn").grid(row=2, column=2)
myLabel3 = Label(root, text = "Welcome to my project").grid(row=1, column=1)

#put them on the screen
#grid it
##they are relative to eachother
#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=2, column=2)
#myLabel3.grid(row=1, column=1)
#
#create an event loop
root.mainloop()
