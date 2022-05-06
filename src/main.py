#It is best practice to use a class name
# to change the value of a class variable. 
#Because if we try to change the class 
#variable’s value by using an object, 
#a new instance variable is created for that
 #particular object, which shadows the class
# variables.


class Student:
    # Class variable
    school_name = 'ABC School '

    # constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

# create Objects
s1 = Student('Emma', 10)
s2 = Student('Jessa', 20)

print('Before')
print(s1.name, s1.roll_no, s1.school_name)
print(s2.name, s2.roll_no, s2.school_name)

# Modify class variable using object reference
s1.school_name = 'PQR School'
print('After')
print(s1.name, s1.roll_no, s1.school_name)
print(s2.name, s2.roll_no, s2.school_name)