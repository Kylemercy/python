class Employee:
  raise_amount = 1.05
  num_emp = 0
  # class Variable 
  def __init__(self,first,last,pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + last + "@company.com"
    Employee.num_emp += 1
    #this increase as the new employee object
#is created  
  def amount_apply(self):
    self.pay = int(self.pay *self.raise_amount)
    print(self.pay)
  
  def display(self):
    print(f"fullname: {self.first} {self.last}")
  
  def __repr__(self):
    return (f"Employee: {self.first},{self.last},{self.pay}")
  
  def __str__(self):
    return (f"{self.display}-{self.email}")
  
#special or dunder method
#use for info overloading
#using the repr and str magic method
#repr is use for debugging by programers
#str is meant for the reader
     
dev1 =Employee("sid","daje",6000)
dev2 = Employee("dash","qote",7000)
#while str is meant for the in user
print(str(dev1))
print(str(dev2))
#repr makes the code more readable 
#for the programmer
print(repr(dev1))
print(repr(dev2))
#or you can do this
print(dev1.__str__())
print(dev1.__repr__())