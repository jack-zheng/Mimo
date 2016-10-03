from tkinter import *

root = Tk()

labelFrame = LabelFrame(root, text="This is a label frame")
labelFrame.pack(fill="both", expand="yes")

left = Label(labelFrame, text="inside the label frame")
left.pack()

root.mainloop()
