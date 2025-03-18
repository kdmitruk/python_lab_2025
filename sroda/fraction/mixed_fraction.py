from fraction import Fraction
class MixedFraction(Fraction):
    def __str__(self):
        whole = self._nominator // self._denominator
        nominator_rest = self._nominator % self._denominator
        if nominator_rest == 0:
            return str(whole)
        elif whole == 0:
            return super().__str__()
        else:
            return f"{whole} {nominator_rest}/{self._denominator}"

    # 4/3 --> 1 1/3
