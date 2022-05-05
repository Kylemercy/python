# Use super()
class Doughnut:
    def __init__(self, flavor, r_in, r_out, topping):
        self.insideRadius   = r_in
        self.outsideRadius  = r_out
        self.topping = topping
        self.flavor = flavor
        
       #  is wrong. YOu do not need 'self'

    def donutarea(self):
        return 3.1416 * (self.outsideRadius ** 2 - self.insideRadius ** 2)
    
    def donutperimeter(self):
        return 2 * 3.1416 * (self.insideRadius +  self.outsideRadius)
    
    def inarea(self):
      return 2* 3.1416*self.insideRadius ** 2
    
      
    
class glazedDonut(Doughnut):
  def __init__(self,flavor,r_in,r_out,topping):
   super().__init__(flavor, r_in, r_out, topping)
                          
emp = glazedDonut("chocolate",4,6,"glazed")
print("We just made a " + emp.topping + ' ' + emp.flavor + " donut.")
print("It's area is: ",emp.donutarea())
print("And it's perimeter is: ")
print(emp.donutperimeter())
print("And the inside hollow area is: ")
print(emp.inarea())