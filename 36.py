from tkinter import *

root = Tk()

group = LabelFrame(root,text = "最好的脚本语言是？",padx = 5,pady = 5)
group.pack(padx = 10,pady = 10)

lang = [("Python",1),("Perl",2),("Ruby",3),("Lua",4)]

v = IntVar()

for x,y in lang:
    b = Radiobutton(group,text = x,variable = v,value = y)
    b.pack(anchor = W)

mainloop()
