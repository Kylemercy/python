def fibonacci(n):
  assert n >= 0 and n == int(n)," invalid input"

  if n in(0,1):
    return n
  else:
    return fibonacci(n-1) + fibonacci(n - 2)
  
  
print(fibonacci(7))
#recursive Fibonacci 