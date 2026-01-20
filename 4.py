import hashlib
data = {"小甲鱼":00000000000,"不二如是":11111111111}

while True:
    name = input("请输入用户名：")
    if name in data:
        print("该用户名已被注册！")
        continue
    else:
        password = input("请输入密码：")
        data[name] = password
    print("目前已注册的用户有：\n-----------------")
    keys = list(data.keys())
    for each in data:
        data[each] = hashlib.md5(bytes(str(data[each]),"utf-8"))
        print(each,data[each].hexdigest(),sep = ":")
    else:
        break
