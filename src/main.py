class Employee:
  raise_amount = 1.02
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
 #creating a class method
  @classmethod
  def set_raise_amount(cls,amount):
    cls.raise_amount = amount

emp1 = Employee("sid","kai",6000)
emp2 = Employee("dats","mods",7590)

print(Employee.num_emp)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
#setting the raise amount
Employee.set_raise_amount(1.07)
#the new raise amount is 1.07
#this is modified using a class method
print(Employee.num_emp)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)