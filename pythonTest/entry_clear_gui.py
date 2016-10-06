from tkinter import *


def clearInput():
    entry.delete(0, END)

top = Tk()
entry = Entry(top)
entry.pack()

button = Button(top, text="Clear", command=clearInput)
button.pack()

mainloop()
