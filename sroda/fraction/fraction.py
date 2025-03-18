from math import lcm
class Fraction:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator
        self.__reduce()

    def is_integer(self):
        return self.nominator % self.denominator == 0

    def __str__(self):
        return f"{self.nominator}/{self.denominator}"

    def __float__(self):
        return float(self.nominator/self.denominator)

    def __reduce(self):
        gcd = abs((self.nominator * self.denominator) // lcm(self.nominator,self.denominator))
        self.nominator //= gcd
        self.denominator //= gcd

    def __mul__(self, other):
        #if other.__class__.__name__ == Fraction.__name__:
        if isinstance(other, Fraction):
            nominator=self.nominator*other.nominator
            denominator=self.denominator*other.denominator
            return Fraction(nominator, denominator)
        elif isinstance(other, int):
            return Fraction(self.nominator * other, self.denominator)
        else:
            return NotImplemented

    def __imul__(self, other):
        self.nominator = self.nominator * other.nominator
        self.denominator = self.denominator * other.denominator
        return self

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return self.__mul__(Fraction(other.denominator, other.nominator))