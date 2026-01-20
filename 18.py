import time
import hashlib

class Member:
    def __init__(self,card,username,password,point,times):
        self.card = card
        self.username = username
        self.password = password
        self.point = point
        self.times = times

class Manage:
    data = []
    def create_card(self):
        username = input("请输入名字：")
        password = input("请输入密码：")
        while len(password) < 6:
            password = input("会员密码不能小于6位，请重新输入：")
        password = p.encrypt(password)
        times = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        point = 0
        card = len(self.data) + 10000
        self.data.append(Member(card,username,password,point,times))
        message = f"开卡成功：{card}->{username}，时间：{times}\n"
        l.log(message)
        print(f"创建成功，卡号为{card}，关联用户->{username}\n")

    def change_password(self):
        a = int(input("请输入卡号："))
        b = input("请输入密码：")
        for each in self.data:
            if each.card == a and each.password == p.encrypt(b):
                _ = input("请输入新密码：")
                while len(_) < 6:
                    _ = input("会员密码不能小于6位，请重新输入：")
                each.password = p.encrypt(_)
                times = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                message = f"修改密码：卡号->{each.card}，时间：{times}\n"
                l.log(message)
                print("密码修改成功\n")
                break
        else:
            print("卡号或密码不正确！")
        
    def pay(self):
        a = int(input("请输入卡号："))
        b = input("请输入密码：")
        for each in self.data:
            if each.card == a and each.password == p.encrypt(b):
                c = int(input("请输入支付金额："))
                each.point += c
                print(f"卡号{each.card}当前的消费积分为：{each.point}\n")
                times = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                message = f"积分累计：卡号->{each.card}，+{each.point}分，时间：{times}\n"
                l.log(message)

    def find_point(self):
        a = int(input("请输入卡号："))
        b = input("请输入密码：")
        for each in self.data:
            if each.card == a and each.password == p.encrypt(b):
                print(f"卡号{each.card}当前的消费积分为：{each.point}\n")

class PasswdMixin(Manage):
    def encrypt(self,password):
        bstr = bytes(password,"utf-8")
        ciphertext = hashlib.md5(bstr).hexdigest()
        return ciphertext
    
class LoggerMixin(Manage):
    def log(self,message,filename = "log.txt"):
        with open(filename,"a") as f:
            f.write(message)

manage = Manage()
p = PasswdMixin()
l = LoggerMixin()

print("欢迎使用鱼C超市会员管理系统\n")
while True:
    x = input("1.创建新卡；2.修改密码；3.商品支付；4.积分查询；5.退出程序:")
    if x == "1":
        manage.create_card()
    elif x == "2":
        manage.change_password()
    elif x == "3":
        manage.pay()
    elif x == "4":
        manage.find_point()
    elif x == "5":
        print("感谢使用鱼C超市会员管理系统")
        break
