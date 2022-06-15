#checking of two words are anagram
''' One string is an anagram of another
 if the second is simply a rearrangement
 of the first. For example,
  'heart' and 'earth' are anagram   '''
def anagram(s1,s2):
  a_list1 = list(s1)
  a_list2 = list(s2)
  
  a_list1.sort()
  a_list2.sort()
# here the list i already sorted out'''  
  matches = True
  pos = 0
  
  while pos < len(s1) and matches:
    if a_list1[pos] == a_list2[pos]:
      pos += 1
    else:
      matches = False
   #therefore the loops break
  return "Not an anagram."


word = anagram('abcde','ecad')
print(word)
    
# writing an anagram using sorting and comparing m
#method   
  
    
  