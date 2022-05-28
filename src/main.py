def outer_func(message):
  msg = message
  def inner_fun():
    print(msg)
  
  return inner_fun
  #lwts not execute the inner fun

#cloures

my_fun = outer_func("hi")
my_hello = outer_func("hello")
my_fun()
my_hello()