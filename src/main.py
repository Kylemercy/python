#static method
#it can be defined using
#the @staticmethod decorator or 
#staticmethod() function.


#using static method function
class Test:
  @staticmethod
  def static1():
    print("static method 1")
  
  def static2():
    Test.static1()
  
  
  @classmethod
  def class_method(cls):
    cls.static2()

test = Test()
test.class_method()
  
  
  
