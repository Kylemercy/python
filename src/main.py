#high- order function
#if a function accept another function as agurment
#returns it as results it is called ahiger order 
#function

def square(x):

  return x*x

def cube(x):
  return x*x*x


def my_map(square,arg_list):
  result = []
  for i in arg_list:
    result.append(square (i))
  
  return result
  
  
  
squares = my_map(square,[1,2,3,4,5])
print(squares)

#to calcute for cube
def my_map(cube,arg_list):
  result = []
  for i in arg_list:
    result.append(cube(i))
  
  return result
  
  
  
squares = my_map(cube,[1,2,3,4,5])
print(squares)