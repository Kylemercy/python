#DECORATORS IN PYTHON
#decorators using class
class decoration_class(object):
  def __init__(self, original):
    self.original = original
  
  def __call__(self,*args,**kwargs):
    print(f"our call method excuted this code before {self.original.__name__}.")
    return self.original(*args,**kwargs)

@decoration_class
def display():
  print("decorated original function.")

@decoration_class
def display_info(name,age):
  print(f"display function ran with argument {name}, and {age}")

display()
print("\n")
display_info("sid",34)
  


