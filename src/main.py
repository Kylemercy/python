#class method
#Used to access or modify the class state
#The class method has a cls parameter 
#which refers to the class.


#Create class method using the @classmethod
# decorator and classmethod() function
#using @classmethod
class Student:
    school_name = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, school_name):
        # class_name.class_variable
        cls.school_name = school_name

    # instance method
    def show(self):
        print(f"{self.name} is {self.age} year's old, School: {Student.school_name}")

jessa = Student('Jessa', 20)
jessa.show()

# change school_name
Student.change_school('XYZ School')
jessa.show()