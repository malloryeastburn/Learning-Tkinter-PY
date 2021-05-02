#Purpose: Creating button widgets

#Import everything from tkinter
from tkinter import *

#needed
root = Tk()

#create a funciton for the button click
def myClick():
    myLabel = Label(root, text="Look! I clicked a button!!")
    myLabel.pack()





#define the thing
myButton = Button(root, text = "Click Me", command=myClick) 
#Button widget options (notes):
#state="DISABLED" 
#padx=40 add x padding
#pady=50 add y padding
#fg="blue" (foreground color(text))
#bg="red" (background color)
#can also use hex color codes


#display the thing
myButton.pack()

root.mainloop()