from tkinter import *
import tkinter

top = Tk()
checkVar1 = IntVar()
checkVar2 = IntVar()
checkVar3 = IntVar()

c1 = Checkbutton(top, text="Music", variable = checkVar1, onvalue=1, offvalue=0,width=20, selectcolor="blue")
c2 = Checkbutton(top, text="Art", variable = checkVar2, onvalue=1, state=DISABLED, justify=LEFT)
c3 = Checkbutton(top, text="Damn", variable = checkVar3, onvalue=1, justify=RIGHT, height=5, width=10)

c1.pack()
c2.pack()
c3.pack()
top.mainloop()
