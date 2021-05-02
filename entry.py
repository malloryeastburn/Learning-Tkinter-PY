#Purpose: Creating Entry widgets

#Import everything from tkinter
from tkinter import *

#needed
root = Tk()

#creating entry widget (input box)
e = Entry(root)
#optional parameters
#width=50
#bg="blue"
#fg="white"
#borderwidth=5
e.pack()
e.insert(0, "Enter Your Name...") #default text in box

#create a funciton for the button click
def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()





#define the thing
myButton = Button(root, text = "Enter Your Name", command=myClick) 

#display the thing
myButton.pack()

root.mainloop()