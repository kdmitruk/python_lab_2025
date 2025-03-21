from math import gcd

class Fraction:
    def __init__(self,nominator,denominator):
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