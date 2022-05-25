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
#creating a sub_class developer
class Developer(Employee):
  def __init__(self,first,last,pay, prog_lang):
    super().__init__(first,last,pay)
    self.prog_lang = prog_lang
  

 
     
dev1 = Developer("sid","kai",6000,"python")
dev2 =Developer("dats","mods",7590,"java")
#print(help(Developer))
print(dev1.pay)
dev1.amount_apply()
print(dev1.email)
dev1.display()
print(dev1.prog_lang)


