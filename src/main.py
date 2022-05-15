import time
def timmer(func):
  def wrapper(*args):
    before = time.time()
    func(*args)
    print("function took",time.time() - before,"seconds")
  return wrapper
    
@timmer  
def run():
  time.sleep(2)
#note this function will run ater 2 seconds

run()
