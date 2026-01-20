
import hashlib

# 功能：获取用户指令
# 返回：字符串，用户指令（1/2/3）
def get_ins():
    print("=====================")
    print("1. 注册")
    print("2. 登录")
    print("3. 退出")
    
    ins = input("请输入指令：")
    while not(ins == '1' or ins == '2' or ins == '3'):
        ins = input("错误！请输入正确的指令：")

    print("=====================")

    return ins


# 功能：MD5加密
# 参数：字符串类型，未加密的明文
# 返回：字符串类型，加密后的密文
def encrypt(plaintext):
    bstr = bytes(plaintext, "utf-8")
    ciphertext = hashlib.md5(bstr).hexdigest()
    return ciphertext


# 功能：模拟论坛注册
def register():
    name = input("请输入用户名：")
    while fishc_db.get(name):
        print("该用户名已存在。")
        name = input("请重新输入用户名：")

    passwd = input("请输入密码：")
    passwd = encrypt(passwd)

    fishc_db[name] = passwd
    print("恭喜，注册成功~")


# 功能：模拟论坛登录
def login():
    name = input("请输入用户名：")
    while not(fishc_db.get(name)):
        print("该用户名不存在。")
        name = input("请重新输入用户名：")

    passwd = input("请输入密码：")
    while fishc_db.get(name) != encrypt(passwd):
        print("密码错误！")
        passwd = input("请重新输入密码：")

    print("恭喜，登录成功~")


# 论坛原始数据库
fishc_db = {}

print("欢迎来到鱼C论坛~")

ins = get_ins()

while ins != '3':
    if ins == '1':
        register()
        
    if ins == '2':
        login()
        
    ins = get_ins()
