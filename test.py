w = input("输入：")
x = []
y = []
f = ""

for each in w:
    if each.isdecimal():
        y.append(each)
    elif each.isalpha():
        x.append(each)

m = "".join(x)
n = "".join(y)

if -1<=len(x)-len(y)<=1:
    if len(x)-len(y)<=0:
        for i in range(len(x)):
            f = "".join((f,n[i],m[i]))
        f = "".join((f,n[i+1]))
    else:
        for i in range(len(y)):
            f = "".join((f,m[i],n[i]))
        f = "".join((f,m[i+1]))
    print("输出：",f)

else:
    print("输出：字符串中数字和字母的数量不满足重新格式化的条件")
