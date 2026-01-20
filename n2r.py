N2R = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]

def num2roman(num):
    r = []
    for v, s in N2R:
        while num >= v:
            r.append(s)
            num = num - v
            # 尝试理解代码，并填写正确的语句
            # 尝试理解代码，并填写正确的语句
        if num == 0:
            break

    return "".join(r)

n = input("请输入一个整数：")
r = num2roman(int(n))
print(f"转换后的结果是：{r}")
