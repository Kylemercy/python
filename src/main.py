def fib_num(n):
  a = 0
  b = 1
  print(a)
  print(b)
  for i in range(2,n):
    
   if n == 1:
    print(a)
  
   else:
    c = a + b
    a = b
    b = c
    print(c)
    
  
  
fib_num(6)
#prints the Fibonacci numbers 