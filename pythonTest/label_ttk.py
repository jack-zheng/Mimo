# seems no distinctly different between the original GUI and ttk
from tkinter import *
import tkinter.ttk as ttk

root = Tk()
label = ttk.Label(root, text='Test', style='BW.TLabel')
label.pack()

mainloop()
