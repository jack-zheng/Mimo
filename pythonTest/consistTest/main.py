import tkinter.ttk as ttk
import tkinter as tki


taskTab = None


def taskTabInit():
    taskTab = tki.Frame(noteBook)
    taskTab.pack()
    entry = tki.Entry(taskTab, bg="blue")
    entry.pack()

root = tki.Tk()

noteBook = ttk.Notebook(root)
taskTabInit()

noteBook.add(taskTab, text="task")
noteBook.pack()

root.mainloop()
