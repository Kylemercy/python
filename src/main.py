#it has both a class and instance variables
class Car:
    # Class variable
    manufacturer = 'BMW'

    def __init__(self, model, price):
        # instance variable
        self.model = model
        self.price = price

# create Object
car = Car('x1', 2500)
print(car.model, car.price, Car.manufacturer)