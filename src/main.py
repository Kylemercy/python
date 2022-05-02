class Cylinder:
    # class attribute
    pi = 3.14
    def __init__(self, radius, height):
        # instance variables
        self.radius = radius
        self.height = height
 
    # instance method
    def volume(self):
        return Cylinder.pi * self.radius**2 * self.height
 
    # class method
    @classmethod
    def description(cls):
        return f'This is a Cylinder class that computes the volume using Pi={cls.pi}'
c1 = Cylinder(4, 2) # create an instance/object
print(f'Volume of Cylinder: {c1.volume()}') # access instance method 
print(Cylinder.description()) # access class method via class
print(c1.description()) # access class method via instance
print(type(c1))