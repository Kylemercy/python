#finding biggest elements in a list using recursion
def find_max(sample,n):
  if n == 1:
    return sample[0]
  return max(sample[n-1],find_max(sample,n-1))

sample = [34,16,80,56,13,89,100,200,6]
n = 9
print(find_max(sample,n))