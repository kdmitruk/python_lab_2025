class Fraction:
    def __init__(self, nominator=None, denominator=None):
        self.nominator = nominator
        self.denominator = denominator

    def is_integer(self):
        return self.nominator % self.denominator == 0

    def __str__(self):
        return f"{self.nominator}/{self.denominator}"


def main():
    f = Fraction()
    f.nominator = 6
    f.denominator = 6
    nf = Fraction()
    nf.nominator = 5
    nf.denominator = 9
    print(f"{f.nominator}/{f.denominator} czy integer: ", f.is_integer())
    print(f"{nf.nominator}/{nf.denominator} czy integer: ", nf.is_integer())
    print(str(f))

if __name__ == '__main__':
    main()