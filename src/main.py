from array import *
arr1 = array('i',[2,4,5,7,8,10])
arr2 = array('d',[1.3,1.7,8.9,3.4])
arr3 = array('u',['a','b','f','g','k'])
arr2.insert(0,2.3)
arr3.insert(1,'e')
print(arr2)
print(arr3)
arr1.insert(3,13)
arr1.insert(0,0)

print(arr1)
#travasal of array
def travasal(array):
  for i in array:
    print(i)
travasal(arr1)
print('\n','accessing elements in an array')
def accessing(array,index):
  if index > len(array):
    print('index i out of range')
  print(array[index])

accessing(arr1,5)
#accessing(arr1,10)
print('\n')
def searching(array, value):
  for i in array:
    if i == value:
      return array.index(value)
  return ("the element does not exist in the array")
print(searching(arr1,5) )
print("searching returns the index of the value")
# deletion of elements in an array using remove
arr2.remove(1.7)
print(arr2)

  
