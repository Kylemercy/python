class employee:
  raise_amount = 1.09
  def __init__(self,first,last,pay):
   
    self.first = first
    self.last = last
    self.pay = pay
    self.email = self.first+ " " + self.last + " @gamil.company"
  
  def full_name(self):
    return self.first + " " + self.last
    return self . email

  def apply_raise(self):
    return self.pay * self.raise_amount
  
  

result = employee("mercy","Jhon",45000)
result1 = employee("chika","Matthew",59000)
result.raise_amount = 2  
print(result1.full_name())
print(result.pay)
print(result.apply_raise())
print(result.__dict__)
  

