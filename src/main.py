class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

    # instance method to access instance variable
    def show(self):
        print('Name:', self.name,"\n" 'Age:', self.age)
c1 = Student("mike",45)
c1.show()