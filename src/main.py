def check_num(num):
  order = len(str(num))
  sum = 0
  temp = num
  while temp >0:
    digit = temp% 10
    sum += digit**order
    
    return num == sum
num = int(input("Enter num "))
if check_num(num):
  print(num,"is an amstrong number")
else:
  print(num,"is not an amstrong number")

  

  
