#creating an array
import array as array
arr = array.array('i',[1,2,3,4,5])
arr1 = array.array('d',[2.0,3.0,5.0,6.0,8.2])
arr2 = array.array('u',['a','b','c','d'])
print(arr)
print(arr1)
print(arr2)
#looping through an array
for i in range(0, len(arr)):
  print(arr[i],end = " ")
print("\n")

for d in range(0, len(arr1)):
  print(arr1[d],end = " ")
print("\n")
  
for u in range(0, len(arr2)):
  print(arr2[u],end = " ")
print("\n")