class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary
#__that is double underscore use to create a private object
     
    def show(self):
        # private members are accessible from a class
        print("Name: ", self.name, 'Salary:', self.__salary)

# creating object of a class
# creating object of a class
emp = Employee('Jessa', 10000)

# accessing private data members
#to Access the private attribute we do this
#we create a method for the attributes as seen
#we then call the method
emp.show() 
#or my using the mangling method which is
# there is no need to create a method
#the private variable can be called directly 




class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

eyu = Employee('messa', 58000)
#to Access the private variable salary
print (eyu._Employee__salary)
#this is called the magling method of accessing
#private variable 