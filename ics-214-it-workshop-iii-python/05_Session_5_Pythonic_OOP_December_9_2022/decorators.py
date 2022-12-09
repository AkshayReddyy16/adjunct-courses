# The definition for decorators goes here.
from time import time


def time_it(decorated_function):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = decorated_function(*args, **kwargs)
        end_time = time()
        print(
            f"Function {decorated_function.__name__} took {end_time - start_time}s to execute."
        )
        return result

    return wrapper
a=[1,2,3,4,5]
b={'a':1,'b':2,'c':3}
def func(*args,**kwargs):
    print(args,kwargs)
fun(*a,**b)
