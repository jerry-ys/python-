class Person:
    def __init__(self,name,job,grade,year,uid):
        self.name = name
        self.job = job
        self.grade = grade
        self.year = year
        self.uid = uid
    def get_uid(self):
        return f"工号：{self.uid}"

    def get_name(self):
        return f"姓名：{self.name}"

    def get_job(self):
        return f"职位：{self.job}"

    def get_grade(self):
        return f"级别：{self.grade}"

    def get_year(self):
        return f"工龄：{self.year}"

    def salary(self):
        if self.job == "E":
            money = 3000 + 500 * self.grade + 50 * self.year
        elif self.job == "T":
            money = 4000 + 800 * self.grade + 100 * self.year
        elif self.job == "M":
            money = 5000 + 1000 * (self.grade + self.year)
        return money

class Main:
    data = []
    j = {"E":[10,"普通员工"],"T":[6,"组长"],"M":[3,"经理"]}
    def save(self):
        name = input("姓名：")
        job = input("职位（E.普通员工；T.组长；M.经理）：")
        year = int(input("工龄："))
        grade = int(input("级别："))
        if job == "E":
            while grade > 10:
                grade = int(input("该职位最高级别为10，请重新录入级别："))
        elif job == "T":
            while grade > 6:
                grade = int(input("该职位最高级别为6，请重新录入级别："))
        elif job == "M":
            while grade > 3:
                grade = int(input("该职位最高级别为3，请重新录入级别："))
        uid = 10000 + len(self.data)
        self.data.append(Person(name,job,grade,year,uid))
        _ = Person(name,job,grade,year,uid).salary()
        print(f"录入成功！姓名：{name}，工号：{uid}，薪资：{_}")

    def find(self):
        _ins = input("1.员工查询；2.职位查询：")
        if _ins == "1":
            a = int(input("请输入工号："))
            for each in self.data:
                if each.uid == a:
                    print(each.get_name())
                    print(each.get_job())
                    print(each.get_grade())
                    print(each.get_year())
                    print(f"薪资：{each.salary()}")
                    break
            else:
                print("该工号不存在！")
        elif _ins == "2":
            count = 0
            x = []
            job = input("职位（E.普通员工；T.组长；M.经理）:")
            for each in self.data:
                if each.job == job:
                    x.append(f"{each.uid}-{each.name}")
                    count += 1
            else:
                if count == 0:
                    print(f"目前公司没有{self.j[job][1]}！")
                else:
                    print(f"目前{self.j[job][1]}共有{count}人")
                    for each in x:
                        print(each)
                    
    def up(self):
        a = int(input("请输入工号："))
        for each in self.data:
            if each.uid == a:
                x = each.salary()
                print(f"{each.name},{each.get_uid()},当前职位：{each.job + str(each.grade)},当前薪资：{x}")
                level = int(input("请输入需要增加的级数："))
                if each.grade + level > self.j[each.job][0]:
                    each.job = list(self.j.keys())[list(self.j.keys()).index(each.job)+1]
                    each.grade = 1
                else:
                    each.grade += level
                _ = each.job + str(each.grade)
                y = each.salary()
                print(f"升级成功!\n{each.name},{each.get_uid()},升级后职位：{_},升级后薪资：{y}（+{y-x}）")
                break
        else:
            print("工号错误")
        
            
    def down(self):
        a = int(input("请输入工号："))
        for each in self.data:
            if each.uid == a:
                x = each.salary()
                print(f"{each.name},{each.get_uid()},当前职位：{each.job + str(each.grade)},当前薪资：{x}")
                level = int(input("请输入需要减少的级数："))
                if each.grade - level < 1:
                    each.job = list(self.j.keys())[list(self.j.keys()).index(each.job)-1]
                    each.grade = self.j[each.job][0]
                else:
                    each.grade -= level
                _ = each.job + str(each.grade)
                y = each.salary()
                print(f"降级成功!\n{each.name},{each.get_uid()},降级后职位：{_},降级后薪资：{y}（-{x-y}）")
                break
        else:
            print("工号错误")

main = Main()
while True:        
    ins = input("1.录入；2.查询；3.升级；4.降级；5.退出：")
    if ins == "1":
        main.save()
    elif ins == "2":
        main.find()
    elif ins == "3":
        main.up()
    elif ins == "4":
        main.down()
    elif ins == "5":
        break
