class Student:
    def __init__(self, name, nationality, ID, age, tuition):
        self.name = name
        self.nationality = nationality
        self.ID = ID
        self.age = age
        self.tuition = tuition
        self.subject = []

    def register_subject(self, sub):
        self.subject.append(sub)

    def pay_tuition(self, money):
        if money < self.tuition:
            print("There is not enough money")
            return
        self.tuition = 0
        print("Paid tuition fee successfully, your excess money is", money - self.tuition)

    def introduce(self):
        print("Name -", self.name)
        print("Nationality -", self.nationality)
        print("ID -", self.ID)
        print("Age -", self.age)
        print("List of subjects -", ", ".join(self.subject))

class Lecturer:
    def __init__(self, name, nationality, ID, age, tuition):
        self.name = name
        self.nationality = nationality
        self.ID = ID
        self.age = age
        self.tuition = tuition
        self.schedule = []

    def add_lecture(self, subject):
        self.schedule.append(subject)
    
    def introduce(self):
        print("Name -", self.name)
        print("Nationality -", self.nationality)
        print("ID -", self.ID)
        print("Age -", self.age)
        print("List of lecture -", ", ".join(self.schedule))

# Sử dụng lớp Student
student = Student("John Doe", "USA", "12345", 20, 5000)
student.register_subject("Math")
student.register_subject("Physics")
student.pay_tuition(6000)
student.introduce()