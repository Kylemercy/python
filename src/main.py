#puthon tricks
words = ["drum","cat","fish"]
counts = [1,4,6]
for word,count in zip(words, counts):
  print(word,":",count)


  
#sum
num = [46,67,89,34,45,67]
print(sum(num))

# set,use to remove duplicate
num1 = [2,4,3,2,5,6,5,2,3,7,8,8,6,9,6]
print(set(num))
print(list(set(num)))
print(sorted(num1))

def my_fun(x):
  return 6*x

print(list(map(my_fun,[1,3,4,2])))
