from tkinter import *

root = Tk()


def mouse(event):
    print("click as %s, %s" % (event.x, event.y))


def key(event):
    print("key press: %s" % repr(event.char))

root = Tk()
frame = Frame(root, width=300, height=300)
frame.bind("<Button-1>", mouse)
frame.pack()

text = Text(root, height=5, width=20)
text.bind("<Control-Key-a>", key)
text.pack()

mainloop()
