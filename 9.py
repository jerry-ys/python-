import random

a = ["A","2","3","4","5","6",'7','8','9','10','J','Q','K']
b = ["♥",'♦','♣','♠']
_ = []
for each in b:
    for i in a:
        _.append(each+i)
_.append("小")
_.append("大")

x = [input("请输入第一位游戏玩家名称：")]
y = [input("请输入第二位游戏玩家名称：")]
z = [input("请输入第三位游戏玩家名称：")]

def fy():
    number = 1
    data = []
    while True:
        while len(_) != 54 - 17 * number:
            _1 = random.randint(1,len(_))-1
            data.append(_[_1])
            del _[_1]
        else:
            number += 1
        if number == 4:
            break
    return data,_

def pri(j,m):
    print(j,"拿到的牌是：",end = "")
    for each in m:
        print(each,end = " ")
    print("\n")
data,_ = fy()
data_1 = data[:17]
data_2 = data[17:34]
data_3 = data[34:]
n = random.randint(1,3)
if n == 1:
    data_1 += _
    print("地主是：",x)
elif n == 2:
    data_2 += _
    print("地主是：",y)
elif n == 3:
    data_3 += _
    print("地主是：",z)
pri(x,data_1)
pri(y,data_2)
pri(z,data_3)
