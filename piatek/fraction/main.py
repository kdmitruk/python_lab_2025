from fraction import Fraction
#import fraction
#import fraction as f

def main():
    fraction1 = Fraction(0,2)
    fraction2 = Fraction(8,6)

    print(str(fraction1))
    print(str(fraction2))
    print(float(fraction2))
    print(fraction1.is_integer())

if __name__ == '__main__':
    main()
