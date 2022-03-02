odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
prime = {1,2,5,7,}
print(odds.union(evens,prime))
print(odds|(evens))
#you can either use union or|
print(odds.intersection(evens,))
# this gives an empty set
print(odds.intersection(prime))
print(evens.intersection(prime))