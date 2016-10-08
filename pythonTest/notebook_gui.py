from tkinter import *
import tkinter.ttk as ttk

root = Tk()
noteBook = ttk.Notebook(root, height=300, width=300, padding=3)
noteBook.pack()

tab1 = ttk.Frame(root)
tab2 = Frame(root)

noteBook.add(tab1, text="page1")
noteBook.add(tab2, text="page2")
noteBook.enable_traversal()

text1 = Text(tab1)
text1.pack()

entry2 = Entry(tab2)
entry2.pack()

mainloop()
