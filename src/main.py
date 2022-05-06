class Student:
    # class variables
    school_name = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def show(self):
        # access instance variables
        print('Student:', self.name, self.age)
        # access class variables
        print('School:', self.school_name)

    @classmethod
    def change_School(cls, name):
        # access class variable
        print('Previous School name:', cls.school_name)
        cls.school_name = name
        print('School name changed to', cls.school_name)

    @staticmethod
    def find_notes(subject_name):
        # can't access instance or class attributes
        return ['chapter 1', 'chapter 2', 'chapter 3']

# create object
jessa = Student('Jessa', 12)
# call instance method
jessa.show()

# call class method
Student.change_School('XYZ School')
jessa.show()
#jessa school changes to (xyz school)