#decorative function
def decoration_fun(original):
  def wrapped_fun():
    return original()
  return wrapped_fun

def display():
  print("decorated original function")

decorative_display = decoration_fun(display)
decorative_display()

  
