import pickle
import time
from pathlib import Path

class Reminder():
    def __init__(self,file = "remider.pkl"):
        self.path = Path(file)
        self.data = self.load_reminder()

    def __getitem__(self,index):
        return self.data[index]

    def __call__(self,a,b,c,d,e):
        self.add_reminder(a,b,c,d,e)

    def save_reminder(self):
        with open(self.path,"wb") as f:
            pickle.dump(self.data,f)

    def load_reminder(self):
        if self.path.exists():
            with open(self.path,"rb") as f:
                return pickle.load(f)
        return []
        
    def add_reminder(self,a,b,c,d,e):
        item = {"text":b,"category":c,"color":d,"complete":False,"priority":e}
        self.data.append(item)
        print(f"已添加提醒事项：{b}，分类：{c}，优先级：{e}")
        self.save_reminder()
    
    def complete_reminder(self,index):
        try:
            self.data[index-1]["complete"] = True
            self.save_reminder()
            print(f'已完成提醒事项：{self.data[index - 1]["text"]}')
        except:
            print('索引无效，请检查提醒事项列表。')

    def delete_reminder(self,index):
        try:
            remove = self.data.pop(index-1)
            self.save_reminder()
            print(f'已删除提醒事项：{remove["text"]}')
        except:
            print('索引无效，请检查提醒事项列表。')

    def list_reminder(self):
        print("提醒事项：")
        for i,each in enumerate(self.data):
            status = "已完成" if each['complete'] else "未完成"
            print(f'{i+1}.{each["text"]}({each["category"]},{each["color"]})({status},优先级:{each["priority"]})')

    def search_reminder(self,action):
        result = [each for each in self.data if action.lower() in each['text'].lower()]
        if result:
            print("搜索结果：")
            for each in result:
                status = "已完成" if each['complete'] else "未完成"
                print(f"{each['text']}({each['category']},{each['color']})({status},优先级:{each['priority']})")

if __name__ == "__main__":
    # 测试阶段为了防止数据重复添加
    # 在每次启动时自动删除pickle文件
    p = Path.cwd() / "reminders.pkl"
    p.unlink(missing_ok=True)

    reminder = Reminder("reminders.pkl")
    
    # 添加提醒
    print("添加提醒 >>>")
    reminder('添加', '买牛奶', '购物', '黄色', 1)
    reminder('添加', '发邮件', '工作', '蓝色', 2)
    reminder('添加', '学编程', '学习', '红色', 1)
    reminder('添加', '打游戏', '娱乐', '紫色', 4)
    reminder('添加', '谈恋爱', '娱乐', '粉色', 1)
    reminder('添加', '打酱油', '购物', '黄色', 3)

    # 删除提醒
    print("\n删除提醒 >>>")
    reminder.delete_reminder(6)

    # 列举提醒
    print("\n列举提醒 >>>")
    reminder.list_reminder()

    # 完成提醒
    print("\n完成提醒 >>>")
    reminder.complete_reminder(5)

    print("\n列举提醒 >>>")
    reminder.list_reminder()

    # 搜索提醒
    print("\n搜索提醒 >>>")
    reminder.search_reminder("编程")
