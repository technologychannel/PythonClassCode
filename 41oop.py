# Class
class Student:
    def __init__(self,name, grade):
        self.name = name
        self.grade = grade
    
    def get_info(self):
        return f"Name is {self.name} and grade is {self.grade}"
    
    def is_passed(self):
        if self.grade >=60:
            return True
        else:
            return False

# Object

s1 = Student(name="Bishworaj",grade=50)
s2 = Student(name="Hari",grade=20)
s3 = Student(name="Sita",grade=60)

print(s1.get_info())
print(s2.get_info())
print(s3.get_info())

print(s1.is_passed())
print(s2.is_passed())
print(s3.is_passed())