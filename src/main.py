class Employee:
  
  def __init__(self,first,last,pay):
    self.first = first
    self.last = last
    self.pay = pay
    
 
  @property
  def fullname(self):
    return "{} {}". format(self.first,self.last)
#the property decorator allows us to create a 
#method which can still be called as an attribute
#example creating an email method but can still
#be called as an attribute instead of a method
  @property
  def email(self):
     return "{}{}@email.com". format(self.first,self.last)
#setter
  @fullname.setter
  def fullname(self,name):
    first,last = name.split(' ')
#(this will split the name given as a single
# unit into fist,and last)
    self.first = first
    self.last = last
  @fullname.deleter
  def fullname(self):
    print("Deleted!")
    self.first = None
    self.last = None
  
    
  
  
dev1 = Employee("han","san",4500)
dv2 = Employee("sid","fax",5000)
dev1.fullname = "jake mike"
del(dev1.fullname)
print (dev1.fullname)
print(dev1.email)