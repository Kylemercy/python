#DECORATORS IN PYTHON
def decoration_fun(original):
  def wrapper_fun(*args,**kwargs):
    #args and kwargs allows our function to 
    #acept more than one positional argument
  
    print(f"our wrapper function excuted this code before {original.__name__}.")
    return original(*args,**kwargs)
  return wrapper_fun

@decoration_fun
def display():
  print("decorated original function.")

@decoration_fun
def display_info(name,age):
  print(f"display function ran with argument {name}, and {age}")

  


display()
print("\n")
display_info("joy",34)

