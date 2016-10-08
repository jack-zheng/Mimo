import tkinter as tki


class TaskTab():
    def __init__(self, noteBook):
        self.frame = tki.Frame(noteBook)
        self.frame.pack()
        self.entry = tki.Entry(self.frame, bg="blue")
        self.entry.pack()
