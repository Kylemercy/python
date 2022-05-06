class Student:
    # Class variable
    school_name = 'ABC School '

    # constructor
    def __init__(self, name):
        self.name = name
        # access class variable inside constructor using self
        print(self.school_name)
        # access using class name
        print(Student.school_name)

# create Object
s1 = Student('Emma')