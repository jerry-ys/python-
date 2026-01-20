class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __eq__(self, other):
        return self.score == other.score

    def __ne__(self, other):
        return self.score != other.score

    def __lt__(self, other):
        return self.score < other.score

    def __le__(self, other):
        return self.score <= other.score

    def __gt__(self, other):
        return self.score > other.score

    def __ge__(self, other):
        return self.score >= other.score


class StudentManager:
    def __init__(self, init_id=100):
        self.students = {}
        self.stu_id = init_id

    def add_student(self, student):
        self.students[self.stu_id] = student
        print(f"添加成功，{student.name}->ID:{self.stu_id}")
        self.stu_id += 1

    def update_score(self, stu_id, new_score):
        if self.students.get(stu_id):
            self.students[stu_id].score = new_score
        else:
            raise NameError("没有该ID")

    def find_student(self, name):
        for each in list(self.students.values()):
            if each.name == name:
                return each
        else:
            raise NameError("未查到该学生！")
        
    def delete_student(self, stu_id):
        if self.students.get(stu_id):
            print(f"删除成功，{self.students[stu_id].name}->ID:{stu_id}")
            del self.students[stu_id]
        else:
            raise NameError("没有该ID")

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < len(self.students):
            _id = list(self.students.keys())[self.value]
            self.value += 1
            return self.students[_id]
        else:
            raise StopIteration

    def __contains__(self, name):
        for each in list(self.students.values()):
            if each.name == name:
                return True
        else:
            return False

    def __len__(self):
        return len(self.students)

if __name__ == "__main__":
    # 初始学号ID设置为100
    manager = StudentManager(100)

    # 添加学生
    s1 = Student("小甲鱼", 666)
    s2 = Student("不二如是", 888)
    s3 = Student("张三李四", 233)
    manager.add_student(s1)
    manager.add_student(s2)
    manager.add_student(s3)

    # 更新学生成绩
    manager.update_score(100, 999)

    # 查找学生
    target = manager.find_student("小甲鱼")
    print(f"查找 -> {target.name}，成绩: {target.score}")

    # 删除学生
    manager.delete_student(102)

    # 迭代学生列表
    for student in manager:
        print(f"迭代 -> 姓名：{student.name}，成绩: {student.score}")

    # 检查学生是否在列表中
    print("小甲鱼" in manager)

    # 获取学生数量
    print(len(manager))

    # 学生之间的成绩PK
    print(s1 > s2)
