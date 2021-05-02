#Purpose: Create a calculator

from tkinter import *

root = Tk()

#change title
root.title("Simple Calculator")

e=Entry(root, width=60, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
def clear_click():
    e.delete(0,END)
def add_click():
    firstNum = e.get()
    global num1
    global button
    button = "add"
    num1 = int(firstNum)
    e.delete(0,END)
def equal_click():
    num2 = e.get()
    e.delete(0,END)
    if button == "add":
        total = num1 + int(num2)
    elif button == "subtract":
        total = num1 - int(num2)
    elif button == "multiply":
        total = num1 * int(num2)
    else:
        if num2 != "0":
            total = num1 / float(num2)
        else:
            total = "ERROR"
    
    e.insert(0, total)
def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))
    return
def subtract_click():
    firstNum = e.get()
    global num1
    global button
    button = "subtract"
    num1 = int(firstNum)
    e.delete(0,END)
    return
def multiply_click():
    firstNum = e.get()
    global num1
    global button
    button = "multiply"
    num1 = int(firstNum)
    e.delete(0,END)
    return
def divide_click():
    firstNum = e.get()
    global num1
    global button
    button = "divide"
    num1 = int(firstNum)
    e.delete(0,END)
    return
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_clear = Button(root, text="Clear", padx=29, pady=20, command=clear_click)
button_add = Button(root, text="+", padx=38, pady=20, command=add_click)
button_subtract = Button(root, text="-", padx=39, pady=20, command=subtract_click)
button_multiply = Button(root, text="x", padx=39, pady=20, command=multiply_click)
button_divide = Button(root, text="/", padx=39, pady=20, command=divide_click)
button_equal = Button(root, text="=", padx=39, pady=20, command=equal_click)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_0.grid(row=4,column=1)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2,column=3)
button_multiply.grid(row=3,column=3)
button_divide.grid(row=4,column=3)

button_equal.grid(row=4,column=2)
button_clear.grid(row=4,column=0)


#loop program

root.mainloop()