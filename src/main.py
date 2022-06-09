#creating an array
import array as array
# accessing an array
x = list(range(1,100,2))
#this only print 50 elements
new_array = array.array('i',x)
for i in range(0,len(x)):
  print(new_array[i],end = ",")
#acessing the position of an element using its
#index
print("\n")
print(new_array[28])