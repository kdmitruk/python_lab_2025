class Fraction:
    def __init__(self,nominator,denominator):
        self.nominator = nominator
        self.denominator = denominator

    def is_integer(self):
        return self.nominator % self.denominator == 0

def main():
    fraction = Fraction(2,2)
    fraction2 = Fraction(3,4)
    print(f"{fraction.nominator}/{fraction.denominator}")
    print(f"{fraction2.nominator}/{fraction2.denominator}")
    print(fraction.is_integer())

if __name__ == '__main__':
    main()
