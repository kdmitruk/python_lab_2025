from fraction import Fraction

def main():
    f = Fraction(4,7)
    nf = Fraction(45,81)
    print(f"{f.nominator}/{f.denominator} czy integer: ", f.is_integer())
    print(f"{nf.nominator}/{nf.denominator} czy integer: ", nf.is_integer())
    print(str(f))
    print(float(f), float(nf))
    print(f*nf)
    for _ in range(3):
        f *= nf
    print(f)
    print(2*f)
    print(Fraction(1, 2) / Fraction(3, 4))
if __name__ == '__main__':
    main()