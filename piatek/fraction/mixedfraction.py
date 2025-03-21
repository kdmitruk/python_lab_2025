from typing import override

from fraction import Fraction


class MixedFraction(Fraction):

    # def __init__(self, whole, nominator, denominator):
    #     super().__init__(whole * denominator + nominator, denominator)

    @override
    def __str__(self):
        if self.is_integer():
            return f"{self.nominator}"
        whole = self.nominator // self.denominator
        if whole == 0:
            return super().__str__()
        rest = self.nominator % self.denominator
        return f"{whole} {rest}/{self.denominator}"