from tkinter import *

def callback():
    var.set("吹吧你，我才不信呢~")

root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set("你所下载的内容含有未成年人限制！\n请满十八")
textLabel = Label(frame1,textvariable = var,
                  justify = LEFT,
                  padx = 10)
textLabel.pack(side = LEFT)

photo = PhotoImage(file = "6.png")
imgLabel = Label(frame1,image = photo)
imgLabel.pack(side = RIGHT)

thebutton = Button(frame2,text='我已满18周岁',command = callback)
thebutton.pack()

frame1.pack(padx = 10,pady = 10)
frame2.pack(padx = 10,pady = 10)

mainloop()
