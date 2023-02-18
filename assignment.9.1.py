class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.den = d

    def show(self):
        print(self.num, '/', self.den)

    def mul(self, f):
        result = Fraction(None, None)
        result.num = self.num * f.num
        result.den = self.den * f.den
        return result

    def sum(self, f):
        result = Fraction(None, None)
        result.num = (self.num * f.den) + (f.num * self.den)
        result.den = (self.den * f.den)
        return result

    def div(self, f):
        result = Fraction(None, None)
        result.num = (self.den * f.den)
        result.den = (self.den * f.num)
        return result

    def sub(self, f):
        result = Fraction(None, None)
        result.num = (self.num * f.den) - (self.den * f.num)
        result.den = self.den * f.den
        return result

fraction1 = Fraction(2, 3)
fraction1.show()
fraction2 = Fraction(3, 5)
fraction2.show()
result_mul = fraction1.mul(fraction2)
result_mul.show()
result_sum = fraction1.sum(fraction2)
result_sum.show()
result_div = fraction1.div(fraction2)
result_div.show()
result_sub = fraction1.sub(fraction2)
result_sub.show()