import time
def timmer(func):
  def wrapper(*args,**kwargs):
    start = time.time()
    rv =  func(*args)
    total= time.time() - start
    print("time: ",total)
    return rv
  return wrapper
    
@timmer  
def test():
  for _ in range(1000):
    pass
@timmer
def t2():
  time.sleep(2)


  
#note this function will run ater 2 seconds

test()
t2()
