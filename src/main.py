def binary_search(my_list,target):
  low = 0
  high = len(my_list) - 1
  while low<= high:
      mid = (low + high)//2
      guess = my_list[mid]
      if guess == target:
        return mid
      if mid >= target:
        high = mid - 1
      
      else:
        low =  mid +1
  return None
      
my_list = [1,2,6,7,8,8,9]
lists = binary_search(my_list,7)  
print(lists)
