from typing import Callable

def logging(f: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print("func is beginning", f)
        return f(*args, **kwargs)
    return wrapper
@logging
def greet(message):
    print(message)

greet('hello')
