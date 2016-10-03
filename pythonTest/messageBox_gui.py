from tkinter import *
from tkinter import messagebox

top = Tk()


def hello():
    messagebox.showinfo("Say Hello", "hello world !")


b1 = Button(top, text="Say", command=hello)
b1.pack()

top.mainloop()
