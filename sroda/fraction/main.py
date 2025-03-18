class Fraction:
    nominator = None
    denominator = None



def main():
    f = Fraction()
    f.nominator = 3
    f.denominator = 7
    nf = Fraction()
    nf.nominator = 5
    nf.denominator = 9
    print(f"{f.nominator}/{f.denominator}")
    print(f"{nf.nominator}/{nf.denominator}")


if __name__ == '__main__':
    main()