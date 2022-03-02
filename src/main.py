num1 = {1,5,7,6,3,8,2}
num2 = {1,5,2,11,15}
diff = num1.difference(num2)
print(diff)
# this print the number that is in num1
#but not in num2
diff2 = num2.difference(num1)
print(diff2)
#this also print numberin num2 but not
#in num1
seta = num2.symmetric_difference(num1)
print(seta)
#this print all the numbers that are not found in
# num1 and num2
# that it combines their differences
num1.update(num2)
print(num1)
