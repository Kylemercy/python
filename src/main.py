def outer_func():
  msg = "hi"
  def inner_fun():
    print(msg)
  
    print("world")
  
  return inner_fun()

outer_func()
  
