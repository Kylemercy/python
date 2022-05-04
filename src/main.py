#using constructor to count
class Employee:
  count = 0
  def __init__(self):
    Employee.count += 1
    
    
emp2 = Employee()
emp2 = Employee()
emp2 = Employee()
print(f"The number of employees is : {Employee.count}")