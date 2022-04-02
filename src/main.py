class employee:
  num_emp = 0

  raise_amount = 1.09
  def __init__(self,first,last,pay):
   
    self.first = first
    self.last = last
    self.pay = pay
    self.email = self.first+ " " + self.last + " @gamil.company"
    employee.num_emp += 1
  def full_name(self):
    return self.first + " " + self.last
    return self . email

  def apply_raise(self):
    return self.pay * self.raise_amount
  
  # how to create a class method
  @classmethod
  def set_raise(cls, amount):
    cls.set_raise = amount
  @classmethod
  def from_string(cls,emp_rec):
    first,last,pay = emp_rec.split("_")  
    return cls(first,last,pay)
  

  @staticmethod
  def workday(day):
     if day.weekday()== 5 or day.weekday() == 6:
       return " its weekend enjoy your weekend"
     else:
       return " its a workday be productive"

import datetime
my_work = datetime.date(2022,3,10)
print(employee.workday(my_work))
     
     
   


