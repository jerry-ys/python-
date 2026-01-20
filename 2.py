w = input("输入一个英文句子：")
m = []
n = ""

w = w.strip().split(" ")
for each in w:
    if each != "":
        m.append(each)

m = list(reversed(m))
for each in m:
    n = n + each + " "
n = n.strip()
print(n)
