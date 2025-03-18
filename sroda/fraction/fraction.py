from math import lcm
class Fraction:
    def __init__(self, nominator, denominator):
        if denominator == 0:
            raise ValueError("Denominator = 0")
        self.nominator = nominator
        self.denominator = denominator
        if nominator != 0:
            self.__reduce()

    def is_integer(self):
        return self.nominator % self.denominator == 0

    def __str__(self):
        return f"{self.nominator}/{self.denominator}"

    def __float__(self):
        return float(self.nominator/self.denominator)

    def __operation(self, other, operand):
        return Fraction(operand(self.nominator*other.denominator, other.nominator * self.denominator),self.denominator*other.denominator)

    def __add__(self, other):
        # return Fraction(self.nominator*other.denominator + other.nominator * self.denominator,self.denominator*other.denominator)
        return self.__operation(other,lambda a,b: a+b)

    def __sub__(self, other):
        # return Fraction(self.nominator*other.denominator - other.nominator * self.denominator,self.denominator*other.denominator)
        return self.__operation(other, lambda a,b : a-b)

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
        if other.nominator == 0:
            raise ZeroDivisionError("Dzielenie przez 0")
        return self.__mul__(Fraction(other.denominator, other.nominator))
