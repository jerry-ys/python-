a = ["A","2","3","4","5","6",'7','8','9','10','J','Q','K']
b = ["♥",'♦','♣','♠']
_ = []
for each in b:
    for i in a:
        _.append(each+i)
_.append("小")
_.append("大")
print(_)

x = input("请出牌（空格间隔，退出请输入Q）：").split(" ")
while x != ["Q"]:
    if len(x) == 2:
        if "小" in x and "大" in x:
            print("符合规则：火箭")
        elif x[0][1] == x[1][1]:
            print("符合规则：对牌")
        else:
            print("不符合规则")
    elif len(x) == 3:
        if x[0][1] == x[1][1] == x[2][1]:
            print("符合规则：三张牌相同")
        else:
            print("不符合规则")
    elif len(x) == 4:
        if x[0][1] == x[1][1] == x[2][1] == x[3][1]:
            print("符合规则：炸弹")
        else:
            print("不符合规则")
    x = input("请出牌（空格间隔，退出请输入Q）：").split(" ")        
