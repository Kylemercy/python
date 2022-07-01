# finding the greatest common divisor of two numbers
# finding gcd using elucidean algorithm
def gcd(x,y):
  assert int(x) == x and int(y) == y,"Number must be integers only"
  if x < 0:
    x = -1 * x
  if y < 0:
    y = -1 * y
  
  if y == 0:
    return x
  
  
  else:
    return gcd(y,x%y)

print(gcd(45.0,-3.6))
  
  
  

  
