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
    return (self.pay)
  
  def fullname(self):
    return "{} {}". format(self.first,self.last)
  
  def __repr__(self):
    return (f"Employee: {self.first},{self.last},{self.pay}")
  
  def __str__(self):
    return (f"{self.display}-{self.email}")
  
  def __add__(self,other):
    return self.pay + other.pay
 
  def __len__(self):
    return len(self.fullname())
  
  
#special or dunder method
#use for info overloading
#using the repr and str magic method
#repr is use for debugging by programers
#str is meant for the reader
     
dev1 =Employee("sid","daje",6000)
dev2 = Employee("dash","qote",7000)
print(dev1.fullname())
print(dev1+ dev2)
print(len(dev2))
print(dev1.amount_apply())
#note when you use return you have to print out
#your methods

