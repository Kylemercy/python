#linear search
def search(arr,n,d):
  for i in range(0,n):
    if arr[i] == d:
      return  i
#this returns the index of i
  return -1


arr = [1,2,5,6,8,9]
n = len(arr)
d = 10
res = search(arr,n,d)
if (res == -1):
  print("Element not found")
else:
  print("Element found at index ",res)


    
  
