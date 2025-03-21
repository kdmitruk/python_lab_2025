from math import gcd

class Fraction:
    def __init__(self,nominator,denominator):
        if denominator == 0:
            raise ValueError("The denominator is 0")
        self.nominator = nominator
        self.denominator = denominator
        self.__reduce()


    def is_integer(self):
        return self.denominator == 1

    def __str__(self):
        return f"{self.nominator}/{self.denominator}"

    def __float__(self):
        return float(self.nominator/self.denominator)

    def __reduce(self):
        gcd_value=gcd(self.nominator,self.denominator)
        self.nominator//=gcd_value
        self.denominator//=gcd_value

    def __mul__(self, other):
        if isinstance(other, Fraction):
            nom = self.nominator*other.nominator
            den = self.denominator*other.denominator
            return Fraction(nom, den)
        elif isinstance(other, int):
            nom = self.nominator * other
            dem = self.denominator
            return Fraction(nom, dem)
        else:
            return NotImplemented

    def __imul__(self, other):
        self.nominator*=other.nominator
        self.denominator*=other.denominator
        return self

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if other.nominator == 0:
            raise ZeroDivisionError("The nominator is 0")
        return self.__mul__(Fraction(other.denominator, other.nominator))