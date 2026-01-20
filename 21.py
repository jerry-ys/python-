import hashlib

class PasswdMixin:

    def is_calid(self,passwd,require = 6):
        while len(passwd) != require:
            passwd = input(f"密码需为{require}位数字，请重新输入：")
        return passwd

    def to_md5(self,passwd):
        byts = bytes(passwd,"utf-8")
        passwd = hashlib.md5(byts).hexdigest()
        return passwd

class UserManager(PasswdMixin):
    data = {}

    def check_account(self,num,passwd):
        passwd = self.to_md5(passwd)
        if self.data.get(num):
            if self.data[num].passwd == passwd:
                return True
            else:
                return False
        else:
            return False

    def create_account(self):
        name = input("请输入姓名：")
        passwd = input("请输入密码：")
        deposit = int(input("请输入预存款："))
        passwd = self.is_calid(passwd)
        passwd = self.to_md5(passwd)
        num = 88888888 + len(self.data)
        self.data[num] = Account(name,passwd,deposit,num)
        print(f"创建成功，卡号是：{num}")

    def delete_account(self):
        num = int(input("请输入卡号："))
        passwd = input("请输入密码：")
        if self.check_account(num,passwd):
            del self.data[num]
        else:
            print("卡号或密码错误！")

    def get_account(self):
        pass

class Account(UserManager):
    
    def __init__(self,name,passwd,deposit,num):
        self.name = name
        self.passwd = passwd
        self.deposit = deposit
        self.num = num
    
    def confirm_name(self):
        pass

    def confirm_num(self,num):
        if self.data.get(num):
            return True
        else:
            return False

    def confirm_passwd(self,num,passwd):
        passwd = self.to_md5(passwd)
        if self.data[num].passwd == passwd:
            return True
        else:
            return False

    def withdraw(self):
        num = int(input("请输入卡号："))
        passwd = input("请输入密码:")
        if self.confirm_num(num) and self.confirm_passwd(num,passwd):
            deposit = float(input("请输入金额:"))
            self.data[num].deposit -= deposit
            print(f"成功取出{deposit}元")
        else:
            print("卡号或密码错误！")

    def deposit(self):
        num = int(input("请输入卡号："))
        passwd = input("请输入密码：")
        if self.confirm_num(num) and self.confirm_passwd(num,passwd):
            deposit = float(input("请输入金额:"))
            self.data[num].deposit += deposit
            print(f"成功存入{deposit}元")
        else:
            print("卡号或密码错误！")

    def transfer(self):
        num = int(input("请输入卡号："))
        passwd = input("请输入密码：")
        if self.confirm_num(num) and self.confirm_passwd(num,passwd):
            carid = int(input("请输入收款人卡号:"))
            if self.confirm_num(carid):
                _ = float(input("请输入金额:"))
                self.data[num].deposit -= _
                self.data[carid].deposit += _
                print("转账成功。")
            else:
                print("收款人卡号不存在")
        else:
            print("卡号或密码错误！")

    def get_balance(self):
        num = int(input("请输入卡号："))
        passwd = input("请输入密码：")
        if self.confirm_num(num) and self.confirm_passwd(num,passwd):
            print(f"您的余额是：{self.data[num].deposit}")
        else:
            print("卡号或密码错误！")

def main():
    u = UserManager()
    a = Account.__new__(Account)
    while True:
        ins = input("1.创建账户/2.删除账户/3.查询余额/4.存款/5.取款/6.转账/7.退出：")
        if ins == "1":
            u.create_account()
        if ins == "2":
            u.delete_account()
        if ins == "3":
            a.get_balance()
        if ins == "4":
            a.deposit()
        if ins == "5":
            a.withdraw()
        if ins == "6":
            a.transfer()
        if ins == "7":
            break
