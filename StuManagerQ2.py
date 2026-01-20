from pathlib import Path

class Student:
    def __init__(self, stu_id, name, score, age, gender, class_name):
        self.stu_id = stu_id
        self.name = name
        self.score = score
        self.age = age
        self.gender = gender
        self.class_name = class_name

    # 检查输入是否合法
    def validate_input(self):
        while len(self.name) >= 10:
            self.name = input("请重新输入姓名（姓名长度需要小于10个字符）：")
        while self.age < 1 or self.age > 120:
            self.age = input("请重新输入年龄（年龄需要在1~120之间）：")
        while self.gender != "M" or self.gender != "F":
            self.gender = input("请重新输入性别（性别只能填写M或F）：")
        while len(self.class_name) > 10:
            self.class_name = input("请重新输入班级名（班级长度需要小于10个字符）：")

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.score == other.score
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.score < other.score
        return False

    def __le__(self, other):
        if isinstance(other, Student):
            return self.score <= other.score
        return False

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.score > other.score
        return False

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.score >= other.score
        return False


class StudentFileManager:
    def __init__(self, data_file='students.txt'):
        self.data_file = Path(data_file)

    def load_students(self):
        with open(self.data_file,"r") as f:
            print(f.read())

    def save_students(self, students):
        for each in students:
            with open(self.data_file,"a") as f:
                f.write(f"{each.stu_id},{each.name},{each.score},{each.age},{each.gender},{each.class_name}\n")
        

class StudentManager:
    def __init__(self, student_file_manager):
        self.students = {}
        self.student_file_manager = student_file_manager
        self.load_students()

    def load_students(self):
        self.student_file_manager.load_students
        
    def save_students(self):
        student = list(self.students.values())
        self.student_file_manager.save_students(student)
        
    def add_student(self, student):
        self.students[student.stu_id] = student
        print(f"添加成功，{student.name}->ID:{student.stu_id}")
        
    def update_score(self, stu_id, new_score):
        if self.students.get(stu_id):
            self.students[stu_id].score = new_score
        else:
            raise NameError("没有该ID")

    def search_by_name(self, name):
        x = []
        for each in list(self.students.values()):
            if each.name == name:
                x.append(each)
        if x:
            return x
        else:
            raise NameError("未查到该学生！")
        
    def search_by_gender(self, gender):
        x = []
        for each in list(self.students.values()):
            if each.gender == gender:
                x.append(each)
        if x:
            return x
        else:
            raise NameError("未查到该学生！")
        
    def search_by_class(self, class_name):
        x = []
        for each in list(self.students.values()):
            if each.class_name == class_name:
                x.append(each)
        if x:
            return x
        else:
            raise NameError("未查到该学生！")
        
    def delete_student(self, stu_id):
        if stu_id in self.students:
            student = self.students.pop(stu_id)
            print(f"删除成功，{student.name} -> ID：{student.stu_id}")
            del student
        else:
            raise ValueError("ID未找到")

    def __iter__(self):
        self.values = list(self.students.values())
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.values):
            student = self.values[self.index]
            self.index += 1
            return student
        else:
            raise StopIteration

    def __contains__(self, name):
        return any(student.name == name for student in self.students.values())

    def __len__(self):
        return len(self.students)

if __name__ == "__main__":
    file_manager = StudentFileManager()
    manager = StudentManager(file_manager)

    try:
        # 添加学生
        s1 = Student(100, "鱼油A", 594, 20, 'M', 'Class1')
        s2 = Student(101, "鱼油B", 653, 22, 'M', 'Class2')
        s3 = Student(102, "鱼油C", 484, 19, 'F', 'Class3')
        s4 = Student(103, "鱼油C", 655, 21, 'F', 'Class1')
        s5 = Student(104, "鱼油E", 547, 18, 'M', 'Class2')
        s6 = Student(105, "鱼油F", 543, 19, 'F', 'Class3')
        manager.add_student(s1)
        manager.add_student(s2)
        manager.add_student(s3)
        manager.add_student(s4)
        manager.add_student(s5)
        manager.add_student(s6)

        # 更新学生成绩
        manager.update_score(103, 666)

        # 搜索学生
        students_by_name = manager.search_by_name("鱼油C")
        students_by_gender = manager.search_by_gender('F')
        students_by_class = manager.search_by_class("Class2")

        # 输出搜索结果
        print("名字搜索结果：")
        for student in students_by_name:
            print(f"ID：{student.stu_id}，姓名：{student.name}，成绩：{student.score}，年龄：{student.age}，性别：{student.gender}，班级：{student.class_name}")

        print("性别搜索结果：")
        for student in students_by_gender:
            print(f"ID：{student.stu_id}，姓名：{student.name}，成绩：{student.score}，年龄：{student.age}，性别：{student.gender}，班级：{student.class_name}")

        print("班级搜索结果:")
        for student in students_by_class:
            print(f"ID：{student.stu_id}，姓名：{student.name}，成绩：{student.score}，年龄：{student.age}，性别：{student.gender}，班级：{student.class_name}")

        # 删除学生
        manager.delete_student(102)

        # 迭代学生列表
        for student in manager:
            print(f"迭代 -> 姓名：{student.name}，成绩: {student.score}")

        # 获取学生数量
        print(len(manager))

        # 检查学生是否在列表中
        print("小甲鱼" in manager)


        # 学生之间的成绩PK
        print(s1 > s2)
        print(s3 < s4)
        print(s5 != s6)

        # 保存数据
        manager.save_students()
        
    except ValueError as e:
        print(f"出错啦：{e}")
