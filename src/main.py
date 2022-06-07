def reversearray(arr,start, end):
  while (start< end):
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    start += 1
    end -= 1
    

def rotate(arr,d):
  if d == 0:
    return
  n = len(arr)
  d = d %n
  reversearray(arr,0,d-1)
  reversearray(arr,d,n-1)
  reversearray(arr,0,n-1)

def printarray(arr):
  for i in range (0,len(arr)):
    print(arr[i],end = " ")


arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
 
rotate(arr, 2)  # Rotate array by 2
printarray(arr)
#reversal algorithm

  

  
