class Fraction:
    def __init__(self, nominator=None, denominator=None):
        self.nominator = nominator
        self.denominator = denominator

    def is_integer(self):
        return self.nominator % self.denominator == 0

    def __str__(self):
        return f"{self.nominator}/{self.denominator}"

    def __float__(self):
        return float(self.nominator/self.denominator)
