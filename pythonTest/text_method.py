from tkinter import *


def select_all(event):
    text.tag_add(SEL, "1.0", END)
    # text.mark_set(INSERT, "1.0")
    # text.see(INSERT)
    return 'break'


def click():
    result = text.selection_get()
    print(result)

root = Tk()
text = Text(root)

text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")

text.pack()

text.bind("<Control-Key-a>", select_all)

button = Button(root, text='select all', command=click)
button.pack()

mainloop()
