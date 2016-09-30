from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("300x100")

def helloCallBack():
	msg = messagebox.showinfo("py title", "py content");

b = Button(top, text="kick me", command = helloCallBack)
b.place(x=0, y=0)
top.mainloop()
