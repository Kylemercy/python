class Car:
    car_name = "Wheeljack"
    def move(self):
        print(self.car_name, "Car is Moving")

class Truck:
    truck_name = "Optimus Prime"
    def move(self):
        print( self.truck_name, "Truck is moving")

class Bike:
    bike_name = "Elita-One"
    def move(self):
        print(self.bike_name, "Bike is moving")

vehicles = [Car(), Truck(), Bike()]

for vehicle in vehicles:
    vehicle.move()
