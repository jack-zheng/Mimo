from tkinter import *
import tkinter.ttk as ttk


def oneStep():
    bar1.step(10)
    bar2.step(10)

root = Tk()

bar1 = ttk.Progressbar(root, value=20, mode='determinate')
bar1.pack()

bar2 = ttk.Progressbar(root, orient='vertical', value=50, mode='indeterminate')
bar2.pack()

bar3 = ttk.Progressbar(root, value=100, mode='determinate')
bar3.pack()

button = Button(root, text='Step', command=oneStep)
button.pack()

mainloop()
