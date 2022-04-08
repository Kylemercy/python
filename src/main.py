def get_second_largest(user_num):
  largest = user_num[0]
  second_largest = user_num[0]
  for i in range(1,len(user_num)):
    if user_num[i] > largest:
      second_largest = largest
      largest = user_num[i]
    elif user_num[i] > second_largest:
      second_largest = user_num[i]
  return second_largest

user_num = [44,11,83,29,25,76,97,88] 
results = get_second_largest(user_num)
print(f"The second largest number is: {results}")
    
 