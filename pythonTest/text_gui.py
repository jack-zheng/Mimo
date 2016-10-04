from tkinter import *


def onclick():
    content = text.get(1.0, "end-1c")
    stripResult = content.strip()
    print("after strip: %s" % repr(stripResult))
    reprResult = repr(content)
    print(reprResult)
    print("repr after strip: %s" % repr(reprResult))
    result = content.splitlines()
    for line in result:
        print("line: %s" % line)
    # print("content: %s" % content)


def getEnd():
    end_point = text.index("end-1c")
    print(type(end_point))
    print(str(end_point))

root = Tk()
text = Text(root)
text.insert(INSERT, "Hello....")
text.insert(END, "Bye Bye....")
text.pack()

text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="black", foreground="green")

button = Button(root, text="Log", command=onclick)
button.pack()

button2 = Button(root, text="End Point", command=getEnd)
button2.pack()

root.mainloop()
