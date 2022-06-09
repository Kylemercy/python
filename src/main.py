#creating an array
import array as array
arr = array.array('i',[1,2,3,4,5,6])
for i in range (0,len(arr)):
  print(arr[i],end = " ")
arr.append(8)
print ("\n")
for i in range (0,len(arr)):
  print(arr[i],end = " ")
arr.insert(4,9)
print ("\n")
for i in range (0,len(arr)):
  print(arr[i],end = " ")
  #adding elements in array
#this is done using insert and append
#updating an element in an array

new_array = array.array('i',[1,2,2,4,5,6])
#this is uae to cahnge an element in an array
#exaple 2 repeats itself it can b changed
# this is done using its index
new_array[2] = 8
print("\n")
for i in range (0,len(new_array)):
  print(new_array[i],end = " ")
