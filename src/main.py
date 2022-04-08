def divisible_by_3and5(num):
  result = [ ]
  for i in range(num):
    if i % 3 and i % 5 == 0:
      result.append(i)
  return result


num = int(input("Enter a number: "))
total = divisible_by_3and5(num)
print(f"numbers divisible by 3 and 5 in range {num} are:\n", total)
    
  






