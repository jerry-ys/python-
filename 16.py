import tkinter

def get_bases(x,level = 0):
    a = []
    print("-"*level,x,sep = "")
    for each in x.__bases__:
        if each.__bases__[0] != object:
            get_bases(each,level+1)
        else:
            print("-"*(level+1),each,sep = "")

            
