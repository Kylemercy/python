def fibanocci(n):
  assert n >= 0 and n == int(n)," invalid input"

  if n in(0,1):
    return n
  else:
    return fibanocci(n-1) + fibanocci(n - 2)
  
  
print(fibanocci(-1))