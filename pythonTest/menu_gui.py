from tkinter import*

def donothing():
	filewin = Toplevel(root)
	button = Button(filewin, text = "Do nothing button")
	button.pack()

root = Tk()
menuBar = Menu(root)

fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New", command=donothing)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

menuBar.add_cascade(label="File", menu=fileMenu)

editMenu = Menu(menuBar, tearoff=0)
editMenu.add_command(label="Undo", command=donothing)

menuBar.add_cascade(label="Edit", menu=editMenu)

root.config(menu=menuBar)
root.mainloop()
