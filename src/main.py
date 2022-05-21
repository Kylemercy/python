#CLOSURES
def outer_fun():
  msg = "Hello"
  def inner_fun():
    print(msg)
  
  return inner_fun
#this won't exceute as the inner func wasn't
#called using()
outer_fun()
#to execute this we assign it to a variable

my_fun = outer_fun()
my_fun()
# this was executed

#another way is by calling the inner func
  
def outer_fun():
  msg = "Hello"
  def inner_fun():
    print(msg)
  
  return inner_fun()
  #the inner func was called using ()
outer_fun()
# this is now executed
  
