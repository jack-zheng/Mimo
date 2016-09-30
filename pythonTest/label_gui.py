from tkinter import *

root = Tk()

var = StringVar()
label = Label(root, textvariable=var, relief=RAISED)

var.set('Hi, can you see me?!')
label.pack()

root.mainloop()
