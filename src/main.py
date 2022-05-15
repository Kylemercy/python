import time
def before_decorated(func):
  def wrapper(*args):
    print("before")
    func(*args)
    print("after")
  
  return wrapper


class Time():
  @before_decorated
  # for class the decorator is called inside
  #a class

  def decorated_method(self):
    print(time.ctime())

t = Time()
t.decorated_method()
  

  
