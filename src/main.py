def sum_digit(n):
  if n < 0:
    return ("Number must be a positive number")
  
  if n == 0:
    return 0
  
  else:
    return int(n%10) + sum_digit(int(n/10))

print(sum_digit(-5))
  
  
  
