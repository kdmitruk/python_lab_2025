class Fraction:
    nominator = None
    denominator = None

    def is_integer(self):
        return self.nominator % self.denominator == 0

def main():
    fraction = Fraction()
    fraction2 = Fraction()
    fraction.nominator = 2
    fraction.denominator = 2
    fraction2.nominator = 3
    fraction2.denominator = 4
    print(f"{fraction.nominator}/{fraction.denominator}")
    print(f"{fraction2.nominator}/{fraction2.denominator}")
    print(fraction.is_integer())

if __name__ == '__main__':
    main()
