def findsmall(arr):
  smallest = arr[0]
  small_index = 0
  for i in range (0,len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      small_index = i
  return small_index
#this return the imdex of the smallest number
  
def find_sort(arr):
  new_arr = []
  for i in range (len(arr)):
    smallest = findsmall(arr)#index of the smallest
   # number
    new_arr.append(arr.pop(smallest))
    #this remove the smallest number
# which is at position 0
#this continues until all the numbers jave been
#removed
  return new_arr

sort = find_sort([3,5,21,7,2,18,9])
check = findsmall([3,5,21,7,2,18,1,9])
print(check)
#this print the index position of smallest num
print(sort)

    
#slow sort algorithm 