class Car:
  def __init__(self, colour,miles):
    self.colour = colour
    self.miles = miles
  
  def description(self):
    return f"The {self.colour} car has {self.miles:,}."
  


car1 = Car("Red",60_000)
car2 = Car("black",89_000)  
print(car1.description())
print(car2.description())