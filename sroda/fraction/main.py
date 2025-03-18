from fraction import Fraction

def main():
    f = Fraction()
    f.nominator = 7
    f.denominator = 7
    nf = Fraction()
    nf.nominator = 5
    nf.denominator = 9
    print(f"{f.nominator}/{f.denominator} czy integer: ", f.is_integer())
    print(f"{nf.nominator}/{nf.denominator} czy integer: ", nf.is_integer())
    print(str(f))
    print(float(f), float(nf))
if __name__ == '__main__':
    main()