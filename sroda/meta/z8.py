class VerboseValue:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        print("pobrano wartość")
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
        print(f"ustawiono wartość na {value}")

if __name__ == "__main__":
    x = VerboseValue(5)
    x.value = 7
    print(x.value)
    x.value += 1