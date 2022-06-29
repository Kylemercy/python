#recursion
def recursive_method(n):
  if n < 1:
    print("n is lesss than one")
  
  else:
    recursive_method(n-1)
    print(n)

recursive_method(5)
  

  
