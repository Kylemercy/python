class Vehicle:
  def __init__(self, distance, mileage):
    self.distance = distance
    self.mileage = mileage
  
  
  def max_speed(self):
    print(self.distance/self.mileage)
   

ept = Vehicle(500,40)
ept.max_speed()
print(ept.distance)
print(ept.mileage)
  
