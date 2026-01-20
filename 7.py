data = []

def yz(x):
    data.append(x)

def qc():
    if data == []:
        print("栈已空~")
    else:
        print(data[-1])
        del data[-1]

def dy():
    print("栈：")
    for each in data[::-1]:
        print(each)

while True:
    m = input("请输入指令（push/pop/top/exit）:")
    if m == "push":
        yz(input("请输入将要压入栈中的值："))
        dy()
    if m == "pop":
        qc()
        dy()
    if m == "top":
        if data == []:
            print("栈已空~")
        else:
            print(data[-1])
    if m == "exit":
        break
