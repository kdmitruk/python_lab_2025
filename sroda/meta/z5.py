from functools import wraps

def print_decorator(text_before, text_after):
    def decorator(f):
        @wraps(f)
        def inner(*args, **kwargs):
            print(text_before)
            f(*args, **kwargs)
            print(text_after)
        return inner
    return decorator

@print_decorator("before43", "after")
def func(x):
    print(f"middle {x}")

if __name__ == "__main__":
    print(func)
    func(4)