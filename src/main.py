#power of a number
def power(base,exp):
  assert int(xp) ==xp and xp < 0,"exponent must be a positive integer"
  if exp == 0:
    return 1
  if exp == 1:
    return base
  else:
    return base * power(base,exp -1)
  
print(power(2,7))
'''note a each recursive call our exponent(exp)
keeps o decreasing until exp becomes 1, then it 
return te base '''
  
  
