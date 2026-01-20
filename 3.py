print("欢迎进入鱼C电话簿")
T = True
data = {}

while T:
    x = input("请输入命令(I：录入/ C：查询/ D：删除/ P：打印/ E：退出):")
    if x == "I":
        print("—— 录入模式 ——")
        while True:
            name = input("请输入姓名：")
            if name not in data:
                number = input("请输入手机号码：")
                while (not number.isdecimal()) or len(number) != 11:
                    number = input("输入不合法，请重新输入：")
            else:
                print("该姓名已录入，手机号码是：",data[name])
                _ = input("请问是否修改（Y/N）：")
                if _ == "Y":
                    number = input("请输入新的手机号码：")
                    while (not number.isdecimal()) or len(number) != 11:
                        number = input("输入不合法，请重新输入：")
            data[name] = number
            n = input("是否继续录入（Y/N）：")
            if n == "N":
                break
    if x == "C":
        print("—— 查询模式 ——")
        while True:
            fname = input("请输入姓名：")
            if fname in data:
                print(fname,":",data[fname],sep = "")
            else:
                print("查无此人！")
            _c = input("是否继续查询（Y/N）：")
            if _c == "N":
                break
    if x == "D":
        print("—— 删除模式 ——")
        while True:
            dname = input("请输入姓名：")
            if dname in data:
                del data[dname]
            else:
                print("查无此人！")
            _d = input("是否继续删除（Y/N）：")
            if _d == "N":
                break
    if x == "P":
        print("—— 打印模式 ——")
        for each in phone_book:
            print(each, data[each], sep="：")
        print()
    if x == "E":
        break
