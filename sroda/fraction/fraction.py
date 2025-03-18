from math import lcm
class Fraction:
    def __init__(self, nominator, denominator):
        if denominator == 0:
            raise ValueError("Denominator = 0")
        self._nominator = nominator
        self._denominator = denominator
        if nominator != 0:
            self.__reduce()

    def is_integer(self):
        return self._nominator % self._denominator == 0

    def __str__(self):
        return f"{self._nominator}/{self._denominator}"

    def __float__(self):
        return float(self._nominator / self._denominator)

    def __operation(self, other, operand):
        return self.__class__(operand(self._nominator * other._denominator, other._nominator * self._denominator), self._denominator * other._denominator)

    def __add__(self, other):
        # return Fraction(self.nominator*other.denominator + other.nominator * self.denominator,self.denominator*other.denominator)
        return self.__operation(other,lambda a,b: a+b)

    def __sub__(self, other):
        # return Fraction(self.nominator*other.denominator - other.nominator * self.denominator,self.denominator*other.denominator)
        return self.__operation(other, lambda a,b : a-b)

    def __reduce(self):
        gcd = abs((self._nominator * self._denominator) // lcm(self._nominator, self._denominator))
        self._nominator //= gcd
        self._denominator //= gcd

    def __mul__(self, other):
        #if other.__class__.__name__ == Fraction.__name__:
        if isinstance(other, Fraction):
            nominator= self._nominator * other._nominator
            denominator= self._denominator * other._denominator
            return Fraction(nominator, denominator)
        elif isinstance(other, int):
            return Fraction(self._nominator * other, self._denominator)
        else:
            return NotImplemented

    def __imul__(self, other):
        self._nominator = self._nominator * other._nominator
        self._denominator = self._denominator * other._denominator
        return self

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if other._nominator == 0:
            raise ZeroDivisionError("Dzielenie przez 0")
        return self.__mul__(Fraction(other._denominator, other._nominator))
