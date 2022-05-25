class Employee:
  raise_amount = 1.02

  # class Variable
  
  def __init__(self,first,last,pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + last + "@company.com"
  
  
  def amount_apply(self):
    self.pay = int(self.pay *self.raise_amount)
    print(self.pay)
  
  def display(self):
    print(f"fullname: {self.first} {self.last}")
  
 
  
emp1 = Employee("sid","kai",6000)
emp2 = Employee("dats","mods",7590)


print(emp1.email)
emp1.display()
print (emp1.pay)
print(emp1.raise_amount)
emp1.amount_apply()
emp2.amount_apply()
print(emp1.__dict__)