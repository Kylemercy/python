#modifying of class method
class Student:
    school_name = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, school_name):
        cls.school_name = school_name

jessa = Student('Jessa', 20)
print(Student.change_school('XYZ School'))
print(Student.school_name)

# delete class method
del Student.change_school

# call class method
# it will give error
print(Student.change_school('PQR School'))