#checking whether an array is sorted
def array_sorted(a):
  if len(a) == 1:
    return True
  return a[0] <= a[1]
  
  

a = [40,20,30,80]
print(array_sorted(a))


b = [20,30,40,50,80]
print(array_sorted(b))


