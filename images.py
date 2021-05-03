#Icons, images, and buttons

# can not get Pillow to work due to Using OneDrive
from tkinter import *
from Pillow import ImageTk, Image

root = Tk()
root.title("Practice")
#Add an icon
root.iconbitmap("C:\\Users\\mallo\\OneDrive\\Desktop\\images\\rocketIcon.ico")


my_img = ImageTk.PhotoImage(Image.open("C:\\Users\\mallo\\OneDrive\\Desktop\\images\\rocketImg.png"))
my_label = Label(image=my_img)
my_label.pack()





#Exit button
button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()


root.mainloop()