from fraction import Fraction

def main():
    f = Fraction(7,7)
    nf = Fraction(45,81)
    print(f"{f.nominator}/{f.denominator} czy integer: ", f.is_integer())
    print(f"{nf.nominator}/{nf.denominator} czy integer: ", nf.is_integer())
    print(str(f))
    print(float(f), float(nf))
if __name__ == '__main__':
    main()