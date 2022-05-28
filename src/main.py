def outer_func():
  msg = "hi"
  def inner_fun():
    print(msg)
  
    print("world")
  
  return inner_fun
  #lwts not execute the inner fun

#in other to execute the inner function
#the outer function is assigned to a variable
my_fun = outer_func()
print(my_fun.__name__)
#now my_fun is equal to inner func
#when called it executes the inner function
my_fun()

  
