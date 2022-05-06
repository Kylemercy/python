class Vehicle:
  def __init__(self, distance, mileage):
    self.distance = distance
    self.mileage = mileage
  
  
  def max_speed(self):
    print(self.distance//self.mileage)


class Bus(Vehicle):
  def __init__(self, distance, mileage, colour):
    super().__init__(distance, mileage)
    self.colour = colour
  


ept = Vehicle(500,40)
ept.max_speed()
print(ept.distance)
print(ept.mileage)
set = Bus(800,30,"red")
set.max_speed()
print(set.colour)
  
