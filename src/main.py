#returning value from a decorated function
def f1(func):
  def wrapper(*args,**kwargs):
    print("started")
    val = func(*args,**kwargs)
    # asign the function to a variable
    #the function that is being wrapped
    print("ended")
    return val
    
    # the return that variable
  return wrapper

@f1
def f(a,b= 30):
  print(f"{a} is {b} years old.")

f("ada")


@f1
def add(a,b):
  return a + b
print(add(4,5))


