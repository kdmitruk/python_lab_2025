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