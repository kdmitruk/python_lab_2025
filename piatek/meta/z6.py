from time import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Czas wykonywania funkcji {func.__name__} = {end - start}')
        return result
    return wrapper

@measure_time
def foo_bar():
    sum = 0
    for i in range(100000000):
        sum += i

    return sum

def main():
    foo_bar()

if __name__ == '__main__':
    main()