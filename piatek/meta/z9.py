class Money:
    def __init__(self):
        self.value = 0

    def __get__(self, instance, owner):
        # return self.value
        return round(self.value/100, 2)

    def __set__(self, instance, value):
        self.value = value*100

class Wallet():
    money = Money()

def main():
    wallet = Wallet()
    wallet.money = 123
    print(wallet.money)

if __name__ == '__main__':
    main()