#import string
def ispangram(str):
  alphabet = "abcdefghijklmnopqrstvuwxyz"
  for char in alphabet:
    if char not in str.lower():
      return False
  return True

str = " the five boxing wizards jump quickly."
if ispangram(str) == True:
  print("yes its a pangram")
else:
  print("No it's not a pangram")



    
  
