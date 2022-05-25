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
    return cls(first,last,pay)
    
#emp1 = Employee("sid","kai",6000)
#emp2 = Employee("dats","mods",7590)
#when our input is in form of a string format
emp1 = ("sandy_gat_6700")
emp2 =("mike_tarh_8900")
emp3 = ("dirt_xander_4600")

new_emp1 = Employee.from_string(emp1)
new_emp2 = Employee.from_string(emp2)
print(new_emp1.email)
print(new_emp2.email,new_emp2.first)
new_emp1.display()


