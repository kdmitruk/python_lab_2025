class RegistryClass(type):
    registry = {}

    def __new__(cls, name, base, fields):
        created_class = super().__new__(cls,name,base,fields)
        RegistryClass.registry[name] = created_class
        return created_class

class C1(metaclass=RegistryClass):
    def __init__(self):
        self.name = "C1"

def main():
    c1 = C1()
    print(RegistryClass.registry)

if __name__ == '__main__':
    main()