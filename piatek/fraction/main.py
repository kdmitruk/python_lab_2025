class Fraction:
    def __init__(self,nominator,denominator):
        self.nominator = nominator
        self.denominator = denominator

    def is_integer(self):
        return self.nominator % self.denominator == 0

    def __str__(self):
        return f"{self.nominator}/{self.denominator}"

def main():
    fraction = Fraction(2,2)
    fraction2 = Fraction(3,4)

    print(str(fraction))
    print(fraction.is_integer())

if __name__ == '__main__':
    main()
