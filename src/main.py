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
  @classmethod
  #creating a alternative method for if our 
  #input is pass as a string separated by an _
  def from_string(cls,emp_str):
    first,last,pay = emp_str.split("_")
    return cls(first,last,int(pay))

  @staticmethod
  def is_workday(day):
    if day.weekday() == 5 or day.weekday() == 6:
  
      print("its a weekday")
    
    else:
      print("Not a weekday") 
    
emp1 = Employee("sid","kai",6000)
emp2 = Employee("dats","mods",7590)
from datetime import datetime
today = datetime.today()
my_date = datetime.date(today)
print(my_date)
print(Employee.is_workday(my_date))



