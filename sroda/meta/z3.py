class RegisteredClass(type):
    classes = {}
    def __new__(cls, name, base, fields):
        print(name)
        print(base)
        print(fields)
        obj = super().__new__(cls, name, base, fields)
        cls.classes[name] = obj
        return obj

class StandardClass(metaclass=RegisteredClass):
    def __init__(self, a: int):
        self.a = a

class NonStandardClass(StandardClass, metaclass=RegisteredClass):
    def __init__(self, a: str):
        super().__init__()
        self.a = a

class UnregisteredClass:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

if __name__ == "__main__":
    # StandardClass(32)
    print(RegisteredClass.classes)