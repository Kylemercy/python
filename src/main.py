#DIFFERENT WAYS OF CREATING A CLASS VARIABLE
#WITH DIFFERENT CHILD CLASS

class Course:
    # class variable
    course = "Python"

class Student(Course):

    def __init__(self, name):
        self.name = name

    def show_student(self):
        # Accessing class variable of parent class
        print('Before')
        print("Student name:", self.name, "Course Name:", Student.course)
 # changing class variable value of base class
        print('Now')
        Student.course = "Machine Learning"
        print("Student name:", self.name, "Course Name:", Student.course)

# creating object of Student class
stud = Student("Emma")
stud.show_student()