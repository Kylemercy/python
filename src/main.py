class Course:
    # class variable
    course = "Python"

class Student(Course):
    # class variable
    course = "SQL"

    def __init__(self, name):
        self.name = name

    def show_student(self):
        # Accessing class variable in an instance method
        print('Before')
        print("Student name:", self.name,"," ,"Course Name:", Student.course)
        # changing class variable's value in a instance method
        print('Now')
        Student.course = "Machine Learning"
        print("Student name:", self.name,"," ,"Course Name:", Student.course)

# creating object of Student class
stud = Student("Emma")
stud.show_student()

# parent class course name
print('Parent Class Course Name:', Course.course)