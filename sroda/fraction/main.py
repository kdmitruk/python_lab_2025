from fraction import Fraction
from mixed_fraction import MixedFraction
def main():
    f = Fraction(4,7)
    nf = Fraction(45,81)
    #print(f"{f.__nominator}/{f.__denominator} czy integer: ", f.is_integer())
    #print(f"{nf.__nominator}/{nf.__denominator} czy integer: ", nf.is_integer())
    print(str(f))
    print(float(f), float(nf))
    print(f*nf)
    for _ in range(3):
        f *= nf
    print(f)
    print(2*f)
    try:
        ff = Fraction(4, 0)
        print(Fraction(1, 2) / ff)
    except (ZeroDivisionError,ValueError) as e:
        print(e)
    # except ZeroDivisionError as e:
    #     print(str(e))
    # except ValueError as e:
    #     print(e)
    print(MixedFraction(1,2) + MixedFraction(3,4))
    #print(Fraction(1,2) - Fraction(3,4))
    #print(MixedFraction(3,1))

if __name__ == '__main__':
    main()