#converting from decimal to binary
def binary(n):
  assert int(n) == n,"the number must be an integer"
  if n == 0:
    return 0
    # here tje function doesn't return any value
  else:
    return n%2 + 10 * binary(int(n/2))#or use//
    #to divide without using int

print(binary(1.5))
  
