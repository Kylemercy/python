class Vehicle:
  def __init__(self,name, distance, mileage):
    self.name = name
    self.distance = distance
    self.mileage = mileage
  
  
  def sitting_capacity(self, capacity):
    return f"The seating capacity of a {self.name} is {capacity} passengers"
  
    


class Bus(Vehicle):
  def sitting_capacity(self,capacity = 50):
    return super(). sitting_capacity(capacity)
    


ept = Vehicle("Toyota",500,40)
print(ept.distance)
print(ept.mileage)
emp = Bus("Toyota",500,40)
print (emp.sitting_capacity())