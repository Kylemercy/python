#operations in an array
from array import *
#* import everything in array
my_array = array('i',[1,2,5,5,6,7,8,9])
#travasal
for i in my_array:
  print(i)
my_array.append(5)
print(my_array)
#ascessing element using index
print('\n')
print(my_array[2])
#inserting using insert method
my_array.insert(3,11)
print(my_array)
#using extend method
my_array2 = array('i',[20,21,23])
my_array.extend(my_array2)
print(my_array)
#addimg list to an array
my_list = [56,72]
my_array.fromlist(my_list)
print(my_array)
#using remove func
my_array.remove(72)
print(my_array)
#note remove only remove the first occursnce of
#an element 
my_array.pop()
print(my_array)
#reversing an array
print('\n')
my_array.reverse()
print(my_array)
print(my_array.buffer_info())
#shows number of element in the array
#count
print(my_array.count(5) )

