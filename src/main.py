def rotateArray(a,d):
  temp = []
  n = len(a)
  for i in range(d,n):
    temp.append(a[i])
  i = 0
  for i in range(0,d):
    temp.append(a[i])
  return temp


 
arr = [1, 2,9, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end = '>= ')
print(rotateArray(arr, 3))


#rotating a code in left direction
def rotateArray(a,d):
    temp = []
    #first create an empty list
    n=len(a)
    for i in range(d,n):
        temp.append(a[i])
    i = 0
    for i in range (0,d):
        temp.append(a[i])
    a=temp.copy()
    return a
 
arr = [1, 2,9, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, 2))
  
