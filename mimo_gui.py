from tkinter import *
from tkinter import messagebox


def insertSQL():
    print("insert sqlite3")


def nullTaskNamePopup():
    messagebox.showinfo("Warning...", "The task name should not be empty")


def clickInsertButton():
    task_name = entry_task.get()
    if len(task_name) == 0:
        nullTaskNamePopup()
    else:
        insertSQL()

root = Tk()
root.title("Day Task")

# top frame contains task name input blank.
topFrame = Frame(root)
topFrame.pack()

label_task = Label(topFrame, text="task name")
label_task.pack(side=LEFT)

stringVar = StringVar()
entry_task = Entry(topFrame, bd=5, textvariable=stringVar)
entry_task.pack(side=RIGHT)

# middile frame contains 3 element, there are content input, comment input
# and star scale.
midFrame = Frame(root)
midFrame.pack()

textFrame = LabelFrame(midFrame, text="Content...")
textFrame.pack(fill="both", expand="yes")

text_content = Text(textFrame, bd=5, height=7, width=50)
text_content.pack()

entryFrame = LabelFrame(midFrame, text="Comment...")
entryFrame.pack(fill="both", expand="yes")

entry_comment = Entry(entryFrame, bd=5)
entry_comment.pack(fill=X)

# buttom frame contains 'Insert' button and it is on the right side.
buttomFrame = Frame(root)
buttomFrame.pack()

# label
# scoreLabel = Label(buttomFrame, text="Score")
# scoreLabel.pack(side=LEFT)
scaleFrame = LabelFrame(buttomFrame, text="Score...")
scaleFrame.pack(side=LEFT)

# scale
var = DoubleVar()
scale = Scale(scaleFrame, variable=var, orient=HORIZONTAL, length=290)
scale.pack()

# button
insert = Button(buttomFrame, text="Insert", command=clickInsertButton)
insert.pack(side=RIGHT)

mainloop()