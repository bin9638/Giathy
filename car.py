import csv

class Pet:
    def __init__(self,name,age,nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
    def show(self):
        print(f"My name is {self.name} and I'm {self.age}.I'm from {self.nationality}")
#Inheritances: tính kế thừa
class Khanh(Pet):
    def __init__(self,name,age,nationality,color):
        super().__init__(name,age,nationality)
        self.color = color
    def show(self):
        print(f"My name is {self.name} and I'm {self.age}.I'm from {self.nationality} and I'm {self.color}")
    def speak(self):
        print("meow")
class Nghi(Pet):
    def speak(self):
        print("GAU")

p=Pet(name="Khanh",age=18,nationality="Vietnam")
p.show()
k = Khanh("Nghi",18,"Vietname","black")
k.show()
k.speak()