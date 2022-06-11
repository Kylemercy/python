#binary search
def search(arr,n,):
  left = 0#(the first index)
  #low
  right = len(arr) - 1#last index
  # high
  
  while left <= right:
    mid = (left + right)// 2
  
    if arr[mid] == n:
      return mid
    else:
      if arr[mid] < n:
        left = mid + 1
        # here the left index changes from
# zero to mid +1 that is the mid value + 1
# thereby reducing the list
      else:
        right = mid - 1
        #here the mid value is greater than n
# there fore the len of the high is now reduced to
# mid value -1
   
  return -1
arr = [1,2,5,6,8,9,20,67,71,76,80]
n = 76 
res = search(arr,n,)
if (res == -1):
  print("Element not found")
else:
  print("Element found at index ",res)


    
  
