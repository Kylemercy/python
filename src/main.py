from string import ascii_lowercase as alpha_lower
def pangram(s):
  return set(alpha_lower) - set(s.lower()) == set([])
s = input("Enter a sentence: ")
if pangram(s) == True:
    print("The string is a pangram")
else:
    print("the string is not a pangram")
  
#checking a pangram using set