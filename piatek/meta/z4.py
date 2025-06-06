from argparse import ArgumentError


class ForceAttributes(type):
    _allowed_args = ['first_name', 'last_name', 'email']
    def __new__(cls, name, base, fields):
        for key in ForceAttributes._allowed_args:
            if key not in fields:
                raise ArgumentError(None, f'key{key} nie jest na liscie allowed_args')
        return super().__new__(cls,name,base,fields)

class Person(metaclass=ForceAttributes):
    first_name = None
    last_name = None
    email = None

def main():
    person1 = Person()


if __name__ == '__main__':
    main()