def repeat_decorator(num_repeats = 2):
# repeat_decorator should return a 
#function that's a decorator
    def inner_decorator(fn):
        def decorated_fn():
            for i in range(num_repeats):
                fn()
        #fn is function that is being decorated
        # return the new function
        return decorated_fn
# return the decorator that actually takes
# the function in as the input
    return inner_decorator
 
# use the decorator with num_repeats argument 
#set as 5 to repeat the function call 5 times
@repeat_decorator(5)
def hello_world():
    print("Hello world!")
 
# call the function
hello_world()