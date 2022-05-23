
def plus_one(number):
     print(f" First: {number + 1}")
     return number + 1
 
def function_call(function):
     number_to_add = 5
     print(f" Second: {function(number_to_add)}")
     return function(number_to_add)
 
function_call(plus_one)