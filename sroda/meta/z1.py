class Account:
    fields = ["email", "age", "role"]
    def __init__(self, *args, **kwargs):

        self.login = args[0]
        self.password = args[1]
        for key, value in kwargs.items():
            if key in Account.fields:
                setattr(self, key, value)

    def __str__(self):
        ret = f"{self.login}:{self.password}"
        for key in Account.fields:
            if hasattr(self, key):
                ret += f" {key}={getattr(self, key)}"
        return ret

if __name__ == "__main__":
    ac1 = Account("user", "pwd", email="user@example.com", age=31)
    print(ac1)