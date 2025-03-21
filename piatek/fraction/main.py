from fraction import Fraction
from mixedfraction import MixedFraction

def main():
    fraction1 = MixedFraction(1,2)
    fraction2 = MixedFraction(3,4)
    fraction3 = Fraction(1,2)
    fraction4 = Fraction(3,4)
    print(fraction1 + fraction2)
    print(fraction3 + fraction4)


if __name__ == '__main__':
    main()
