class Grocery:
  def __init__(self,name, quantity,price):
    self.name = name
    self.quantity = quantity
    self.price = price
  
  def total(self):
    return self.price*self.quantity


item1 = Grocery("phone",50,7000)
item2= Grocery("laptop",89,9600)
print(item2.total())
print(item1.total())


#the first method or second
#the first is better
class Grocery:
item1.phone = "phone"
item1.quantity = 70
item1.price = 700

item2 = Grocery()
item2.phone = "laptop"
item2.quantity = 60
item2.price = 800


print(item2.calculate(item2.quantity,item2.price))
  
  

  

