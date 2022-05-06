#static method
#it can be defined using
#the @staticmethod decorator or 
#staticmethod() function.


#using static method function
class Employee:
    def sample(x):
        print('Inside static method', x)

# convert to static method
Employee.sample = staticmethod(Employee.sample)
# call static method
Employee.sample(10)