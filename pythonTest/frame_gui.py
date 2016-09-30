from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

b1 = Frame(root)
b1.pack(side = BOTTOM)

red = Button(frame, text="Red", fg="red")
red.pack(side=LEFT)

brown = Button(frame, text="Brown", fg="brown")
brown.pack(side=RIGHT)

blue = Button(frame, text="Blue", fg="blue")
blue.pack(side=LEFT)

black = Button(b1, text="Black", fg="black")
black.pack(side=RIGHT)

pink = Button(b1, text="Pink", fg="pink")
pink.pack(side=BOTTOM)

root.mainloop()
