# base class
class Company:
    def __init__(self):
 # Protected member having a single underscore
        self._project = "NLP"
        

# child class
class Employee(Company):
    def __init__(self, name):
        self.name = name
        #super().__init__()
        Company.__init__(self)
      #this use to inherit the project attribute

    def show(self):
        print("Employee name :", self.name)
   # Accessing protected member in child class
        print("Working on project :", self._project)

c = Employee("Jessa")
c.show()

# Direct access protected data member
print('Project:', c._project)