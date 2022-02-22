def computer_gcd(x,y):
  small = min(x,y)
  gcd = 1
  for i in range(1, small +1):
    if((x%i == 0) and(y% i==0)):
      gcd == i
  return gcd
num1 = int (input("Enter NUM 1: "))
num2 =int(input("Enter NUM 2: "))
gcd = computer_gcd(num1,num2)
print("The gcd of",num1,"and",num2,"is",gcd)
    
  
    
  

 