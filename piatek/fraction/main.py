from fraction import Fraction
#import fraction
#import fraction as f

def main():
    fraction1 = Fraction(5,7)
    fraction2 = Fraction(8,6)

    #fraction1 *= fraction2
    #print(fraction1)
    fraction3 = fraction1 * 5
    fraction4 = 5 * fraction2
    try:
        fraction5 = fraction2 / Fraction(0,1)
        print(fraction5)
    except ZeroDivisionError as error:
        print(error)

    #print(str(fraction1))
   # print(str(fraction2))
    #print(float(fraction2))
   # print(fraction1.is_integer())

if __name__ == '__main__':
    main()
