data = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

keys = input("请输入一个罗马字符：")

def func(keys):
    number = 0
    for i in range(len(keys)):
        if i == 0:
            number = number + data[keys[i]]
            continue
        if data[keys[i]] > data[keys[i-1]]:
            number = number + data[keys[i]] - data[keys[i-1]] * 2
        else:
            number = number + data[keys[i]]
    return number

number = func(keys)
print("转换后的结果是：",number,sep = "")
