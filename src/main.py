def fib_num(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
    
  else:
    return fib_num(n-2) + fib_num(n-1)
  
for i in range(10):
  print(fib_num(i))

  
  
