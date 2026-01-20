class Car:
    def __init__(self,brand,model,platenum,dayrent,carid):
        self.brand = brand
        self.model = model
        self.platenum = platenum
        self.dayrent = dayrent
        self.carid = carid

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_platenum(self):
        return self.platenum

    def get_dayrent(self):
        return self.dayrent

    def get_carid(self):
        return self.carid

class EconomyCar(Car):
    subsidy = 0
        
    def calc_rent(self):
        rent = self.dayrent - self.subsidy
        return rent

class LuxuryCar(Car):
    insurance = 0
    
    def calc_rent(self):
        rent = self.dayrent + self.insurance
        return rent

class SportCar(Car):
    loss = 0
    
    def calc_rent(self):
        rent = self.dayrent + self.loss
        return rent

class SUV(Car):
    subsidy = 0
        
    def calc_rent(self):
        rent = self.dayrent - self.subsidy
        return rent

class CarOperation:
    car = {}
    stocks = {'经济车型': [], '豪华车': [], '跑车': [], 'SUV': []}

    def operate(self):
        print("欢迎使用鱼C汽车租赁程序")
        while True:
            ins = input("\n1.录入汽车；2.租车服务；3.还车服务；4.退出程序：")
            if ins == "1":
                self.register()
            elif ins == "2":
                self.get_stock()
                self.rent_car()
            elif ins == "3":
                self.return_car()
            elif ins == "4":
                break

    def register(self):
        ins = input("\n1.经济车型；2.豪华车；3.跑车；4.SUV：")
        number = int(input("\n请输入需要录入的数量："))
        for i in range(number):
            print(f"\n请录入第{i+1}辆车")
            brand = input("品牌：")
            model = input("型号：")
            platenum = input("车牌：")
            dayrent = int(input("租金："))
            if ins == "1":
                carid = 10000 + len(self.stocks["经济车型"])
                _ = EconomyCar(brand,model,platenum,dayrent,carid)
                _.subsidy = int(input("补贴："))
                self.stocks["经济车型"].append(_)
                self.car[carid] = _
            elif ins == "2":
                carid = 20000 + len(self.stocks["豪华车"])
                _ = LuxuryCar(brand,model,platenum,dayrent,carid)
                _.insurance = int(input("保险："))
                self.stocks["豪华车"].append(_)
                self.car[carid] = _
            elif ins == "3":
                carid = 30000 + len(self.stocks["跑车"])
                _ = SportCar(brand,model,platenum,dayrent,carid)
                _.loss = int(input("损耗："))
                self.stocks["跑车"].append(_)
                self.car[carid] = _
            elif ins == "4":
                carid = 40000 + len(self.stocks["SUV"])
                _ = SUV(brand,model,platenum,dayrent,carid)
                _.subsidy = int(input("补贴："))
                self.stocks["SUV"].append(_)
                self.car[carid] = _

    def get_stock(self):
        keys = list(self.stocks.keys())
        for i in range(len(keys)):
            if i == 0:
                print(f"\n{i+1}.{keys[i]}(享有补贴),共有{len(self.stocks[keys[i]])}辆")
                for each in self.stocks[keys[i]]:
                    print(f"车辆编号：{each.get_carid()}，品牌：{each.get_brand()}，型号：{each.get_model()}，日租金：{each.get_dayrent()}-{each.subsidy}（补贴）元")
            elif i == 1:
                print(f"\n{i+1}.{keys[i]}(需额外购买保险),共有{len(self.stocks[keys[i]])}辆")
                for each in self.stocks[keys[i]]:
                    print(f"车辆编号：{each.get_carid()}，品牌：{each.get_brand()}，型号：{each.get_model()}，日租金：{each.get_dayrent()}+{each.insurance}（保险）元")
            elif i == 2:
                print(f"\n{i+1}.{keys[i]}(需增加损耗费用),共有{len(self.stocks[keys[i]])}辆")
                for each in self.stocks[keys[i]]:
                    print(f"车辆编号：{each.get_carid()}，品牌：{each.get_brand()}，型号：{each.get_model()}，日租金：{each.get_dayrent()}+{each.loss}（损耗）元")
            elif i == 3:
                print(f"\n{i+1}.{keys[i]}(租赁超过7天，享有额外7折优惠),共有{len(self.stocks[keys[i]])}辆")
                for each in self.stocks[keys[i]]:
                    print(f"车辆编号：{each.get_carid()}，品牌：{each.get_brand()}，型号：{each.get_model()}，日租金：{each.get_dayrent()}-{each.subsidy}（补贴）元")

    def rent_car(self):
        carid = int(input("\n请输入需要租赁的车辆编号："))
        if self.cars.get(carid):
            day = int(input("请输入需要租赁的天数："))
            print(f"租赁{day}天，总共需要花费：{self.car[carid].calc_rent() * day}元")
            if carid < 20000:
                del self.stocks["经济车型"][self.stocks["经济车型"].index(self.car[carid])]
            elif carid < 30000:
                del self.stocks["豪华车"][self.stocks["豪华车"].index(self.car[carid])]
            elif carid < 40000:
                del self.stocks["跑车"][self.stocks["跑车"].index(self.car[carid])]
            else:
                del self.stocks["SUV"][self.stocks["SUV"].index(self.car[carid])]
            print("恭喜，租赁成功~")

    def return_car(self):
        carid = int(input("请输入车辆编号："))
        if self.cars.get(carid):
            if carid < 20000:
                self.stocks["经济车型"].append(self.car[carid])
            elif carid < 30000:
                self.stocks["豪华车"].append(self.car[carid])
            elif carid < 40000:
                self.stocks["跑车"].append(self.car[carid])
            else:
                self.stocks["SUV"].append(self.car[carid])
            print("恭喜，还车成功~")
