
x = int(input())
if x % 2 == 0: 
  print(x, " is even.")
  print("Did you know that 2 is the only even number that is prime?")
else:
  print(x, " is odd.") 
  print("Did you know that multiplying two odd numbers " + "always gives an odd result?")
import math
import random
y = int(input("Enter a number: "))
if y <= 0:
  print("sorry negative number is not allowed")
  print("i will use the default number in range 1-10 ")
  y = random.randint(1,10+1)
  
mit =math.sqrt(y)
print(  "the square root of ", y ,"is", round(mit,2))
