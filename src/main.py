#creating an array
import array as array
#slicing an array
x = list(range(1,100,3))
#we have 33 elements here
arr = array.array('i',x)
for i in range(1,len(x)):
  print(arr[i],end= " ")
print("\n")
arr0 = arr[10:20]
for i in range(1,len(arr0)):
  print(arr0[i],end = " ")
# revising a list using slicing
print("\n")
arr1 = arr[::-1]
for i in range(1,len(arr1)):
  print(arr1[i],end = " ")
 #revising the main list 