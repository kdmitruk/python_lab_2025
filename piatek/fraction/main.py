from fraction import Fraction
from mixedfraction import MixedFraction


#import fraction
#import fraction as f

def main():
    fraction1 = Fraction(1,2)
    fraction2 = Fraction(3,4)

    #fraction1 *= fraction2
    #print(fraction1)
    fraction3 = fraction1 * 5
    fraction4 = 5 * fraction2
    try:
        fraction5 = fraction2 / Fraction(1,0)
        print(fraction5)
    except (ZeroDivisionError,ValueError) as error:
        print(error)

    print(fraction1 + fraction2)
    print(MixedFraction(1,1,2))
    #except ValueError as error:
       # print(error)

    #print(str(fraction1))
   # print(str(fraction2))
    #print(float(fraction2))
   # print(fraction1.is_integer())

if __name__ == '__main__':
    main()
