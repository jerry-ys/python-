s = input("输入:")

for i in s[::-1]:
    if int(i) % 2 != 0:
        print("输出：",s[:len(s)-s[::-1].index(i)])
        break
else:
    print("0")