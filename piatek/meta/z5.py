def log_exec(func):
    def wrapper(*args, **kwargs):
        print(f'Rozpoczeto wykonywanie funkcji: {func.__name__}')
        result = func(*args, **kwargs)
        print(f'Zakonczono wykonywanie funkcji: {func.__name__}')
        return result
    return wrapper

@log_exec
def foo_bar(name: str):
    print(f'Hi, {name}')

def main():
    foo_bar('Jan')

if __name__ == '__main__':
    main()