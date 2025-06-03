from functools import wraps
from time import time

def time_decorator(f):
    @wraps(f)
    def inner(*args, **kwargs):
        start = time()
        f(*args, **kwargs)
        end = time()
        print(f"execution time: {end-start}")
    return inner

@time_decorator
def func(x):
    for i in range(100000000):
        pass

if __name__ == "__main__":
    print(func)
    func(4)