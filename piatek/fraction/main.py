class Fraction:
    nominator = None
    denominator = None

def main():
    fraction = Fraction()
    fraction2 = Fraction()
    fraction.nominator = 1
    fraction.denominator = 2
    fraction2.nominator = 3
    fraction2.denominator = 4
    print(f"{fraction.nominator}/{fraction.denominator}")
    print(f"{fraction2.nominator}/{fraction2.denominator}")

if __name__ == '__main__':
    main()
