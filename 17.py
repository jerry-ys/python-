from pathlib import Path
from time import strftime, localtime

def pr(x):
    for each in x.iterdir():
        print(each)
        a.append(each)
        if each.is_dir():
            pr(each)
    return a

class File():
    s = []
    name_size = []
    position = []
    create = []
    modify = []
    visit = []
    _ = []

    def save_data(self,x):
        self.s.append(x.stem)
        self.name_size.append(f"{x.name}({x.stat().st_size}字节)")
        self.position.append(f"位置：{x}")
        self.create.append(strftime("创建时间:%Y-%m-%d %H:%M:%S",localtime(x.stat().st_ctime)))
        self.modify.append(strftime("修改时间:%Y-%m-%d %H:%M:%S",localtime(x.stat().st_mtime)))
        self.visit.append(strftime("访问时间:%Y-%m-%d %H:%M:%S",localtime(x.stat().st_atime)))
    def get_data(self,y):
        self._ = []
        for each in self.s:
            i = 1
            if y == each:
                m = self.s.index(each)
                if self._ == []:
                    self._.append(self.s.index(each))
                else:
                    self._.append(self.s.index(each)+i)
                self.s.pop(m)
                i += 1
        return self._
        
def search(z):
    x = input("请输入想要搜索的文件名：")
    z.get_data(x)
    if len(z._) == 0:
        print("找不到相关文件")
    else:
        i = 1
        for each in z._:
            print(f"找到相关文件（{i}）->{z.name_size[each]}")
            print(z.position[each])
            print(z.create[each])
            print(z.modify[each])
            print(z.visit[each],"\n")
            i += 1

p = Path("D:/target")
a = []  
print("路径结构如下：")
pr(p)
f = File()

for each in a:
    f.save_data(each)
else:
    search(f)
