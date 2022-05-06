class Student:
    # class variables
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    # instance variables
    def show(self):
        print(self.name, self.age, Student.school_name)

    @classmethod
    def change_School(cls, name):
        cls.school_name = name

    @staticmethod
    def find_notes(subject_name):
        return ['chapter 1', 'chapter 2', 'chapter 3']
        
        
# create object
jessa = Student('Jessa', 12)
# call instance method
jessa.show()

# call class method using the class
Student.change_School('XYZ School')
jessa.show()
# call class method using the object
jessa.change_School('PQR School')
jessa.show()
# call static method using the class
Student.find_notes('Math')
# call class method using the object
jessa.find_notes('Math')
#A static method doesn’t have access 
#to the class attribute and instance attributes.
# Therefore, it cannot modify the class or object
# state.therefore nothing is modified 