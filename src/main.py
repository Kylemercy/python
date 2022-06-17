from string import ascii_lowercase as asc_lower
def check_pangram(s):
  
  res = [ ]
  val = set(asc_lower) - set(s.lower())
  for i in val:
    res .append(i)
  return res
  

 
s = input("Enter sentence: ").lower()
txt = check_pangram(s)
print(txt)
  
#a pangram is a string that contains all the
# character of the alphabet 