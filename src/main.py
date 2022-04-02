class Employee:
  num_emp = 0

  raise_amount = 1.74
  def __init__(self,first,last,pay):
   
    self.first = first
    self.last = last
    self.pay = pay
    self.email = self.first+ " " + self.last + " @gamil.company"
    Employee.num_emp += 1
  def full_name(self):
    return self.first + " " + self.last
    

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
class developer(Employee):
  raise_amount = 1.30
  def __init__(self,first,last,pay,pro_lang):
    super().__init__(first,last,pay)
    # you can use the first option or second
    #Employee.__init__(self, first, last,pay)
    self.pro_lang = pro_lang

class Manager(Employee):
  def __init__(self,first,last, pay,employees = None):
    super().__init__(first,last,pay)
    if employees is None:
      self.employees = []
    else:
     self.employees = employees
  def add_emp(self,emp):
    if emp not in self.employees:
      self.employees.append(emp)
      
      
  def remove_emp(self,emp):
    if emp in self.employees:
      self.employees.remove(emp)
    
  def print_emp(self):
    for emp in self.employees:
      print(">>>",emp.full_name())  
  

dv1 = developer("mercy","jang",5000,"Python")
dv2 = developer("kate","san",6000,"java")
mg1 = Manager("sie","dan",6900,[dv1])
print(mg1.email)
print(mg1.full_name())
print(mg1.add_emp(dv2))
print(mg1.print_emp())




     
     
   


