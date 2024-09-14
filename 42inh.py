
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print(f"Name is {self.name}, age is {self.age}")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def get_info(self):
        super().get_info()
        print(f"Grade is {self.grade}")

s1 = Student(name="Bishworaj",age=27, grade=26)
s1.get_info()