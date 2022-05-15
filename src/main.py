def f1(func):
  def wrapper(*args,**kwargs):
    print("started")
    func(*args,**kwargs)
    #the function that is being wrapped
    print("ended")
  return wrapper

@f1
def f(a,b= 30):
  print(f"{a} is {b} years old.")

f("ada")


