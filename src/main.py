class Vehicle:
  colour = " white"

  def __init__(self,name, distance, mileage):
    self.name = name
    self.distance = distance
    self.mileage = mileage
  
  
  def sitting_capacity(self, capacity):
    return f"The seating capacity of a {self.name} is {capacity} passengers"
  
    


class Bus(Vehicle):
  pass

class Car(Vehicle):
  pass



School_bus = Bus("School Volvo", 180, 12)
print(School_bus.colour, School_bus.name, "Distance:", School_bus.distance, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.colour, car.name, "Distance:", car.distance, "Mileage:", car.mileage)

  

    


