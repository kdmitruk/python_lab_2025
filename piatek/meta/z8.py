class VerboseValue:
    def __init__(self, value):
        self.value = value
        print(f'Poczatkowa wartosc: {self.value}')

    def __get__(self, instance, owner):
        print(f'Zwrocono wartosc: {self.value}')
        return self.value

    def __set__(self, instance, value):
        self.value = value
        print(f'Ustawiono wartosc na: {self.value}')

class Foo:
    value = VerboseValue(5)


def main():
    foo = Foo()
    foo.value = 7
    print(foo.value)

    bar = VerboseValue(3)
    bar = 'xyz'

if __name__ == '__main__':
    main()