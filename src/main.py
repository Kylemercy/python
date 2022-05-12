#DECORATORS IN PYTHON
def decoration_fun(original):
  def wrapper_fun():
    print(f"our wrapper function excuted this code before {original.__name__}.")
    return original()
  return wrapper_fun

@decoration_fun
def display():
  print("decorated original function.")
# a shorter format for the above code
#using a decorator @
# now we just have to call the display method
display()
#the both print thesame code
print("\n")
decorative_display = decoration_fun(display)
decorative_display()




  
