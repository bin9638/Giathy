class School:
    def __init__(self, name):
        self.name = name
        self.Students=[]
        self.Teachers=[]
        self.classes=[]

    def add_class(self, v):
        self.classes.append(v)

    def write_classes(self):
        print(f"Classes of school {self.name} are:")
        for cla in self.classes:
            cla.write_name();
        print(f"")

    def add_student(self, v):
        self.Students.append(v)

    def write_students(self):
        print(f"Students of school {self.name} are:")
        for stu in self.Students:
            stu.write_name();
        print(f"")

    def add_teacher(self, v):
        self.Teachers.append(v)

    def write_teachers(self):
        print(f"Teachers of school {self.name} are:")
        for te in self.Teachers:
            te.write_name();
        print(f"")

class Student:
    def __init__(self, name):
        self.name = name

    def write_name(self):
        print(f"Student: {self.name}")

class Teacher:
    def __init__(self, name):
        self.name = name

    def write_name(self):
        print(f"Teacher: {self.name}")

class Class:
    def __init__(self, name):
        self.name = name
        self.list = [];
        self.sum_score = 0
        self.num_students = 0
    
    def write_name(self):
        print(f"Class: {self.name}")

    def add_participants(self, member, score, type):
        self.list.append(member)
        if type == 1:
            self.num_students+=1
            self.sum_score+=score

    def write_participants(self):
        print(f"Members of class {self.name}:")
        for member in  self.list:
            member.write_name()
        print(f"");

    def write_result(self):
        print(f"average score of {self.num_students} students is {self.sum_score / self.num_students}")


Huy = Student("HA AN")
Khanh = Teacher("Khanh dep trai")
OOP = Class("OOP")
OOP.add_participants(Huy, 1, 1)
OOP.add_participants(Khanh, 0, 2)
NUS = School("NUS")
NUS.add_class(OOP)
NUS.add_student(Huy)
NUS.add_teacher(Khanh)
NUS.write_classes()
NUS.write_students()
NUS.write_teachers()
OOP.write_participants()
OOP.write_result()