def arr_reverse(arr,n):
  first = 0
  n = 5
  end = n- 1
  while (first < end):
     temp = arr[first]
     arr[first] = arr[end]
     arr[end] = temp
     first += 1
     end -= 1
  return arr

  
arr = [2,45,6,8,9]  
ti = arr_reverse(arr,5)
print(ti)
'''in the following code, we have assigned the 
value of index 1(start)to the temp variable
 and end index to start index 1. 
 Then we have assigned the value of 
 temp (stored value of index 1 ie 6) to end.
 we then increase start by 1 and decrease end
by 1'''
 