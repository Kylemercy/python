def find_maxnum(n):
  biggest_num = array[0]
  for num in range(1,len(array)):
    if array[num] > biggest_num:
      biggest_num = array[num]
  print(biggest_num)


array = [3,4,1,9,11,163,6,18]
find_maxnum(array)
    
  
