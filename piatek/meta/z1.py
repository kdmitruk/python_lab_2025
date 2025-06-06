from argparse import ArgumentError


class Account:
    _allowed_args = ['first_name', 'last_name', 'email']

    def __init__(self, login, password, **kwargs):
        self.login = login
        self.password = password

        for key, value in kwargs.items():
            if key in self._allowed_args:
                setattr(self, key, value)
            else:
                raise Exception(f'{key} nie znajduje sie w liscie dozwolonych argumentow')

    def __str__(self):
        arguments = f'\nlogin: {self.login}, haslo: {self.password}'

        for arg in self._allowed_args:
            if hasattr(self, arg):
                arguments += f', {arg}: {getattr(self, arg)}'

        return arguments

def main():
    acc = Account('login', '123', emailll='mail@umcs.pl')
    print(acc)

if __name__ == '__main__':
    main()