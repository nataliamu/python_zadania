class ComplexNumber:
    def __init__(self, re, im):
        self.numberRe = re
        self.numberIm = im

    def __add__(self, other):
        return ComplexNumber(other.numberRe + self.numberRe, other.numberIm + self.numberIm)

    def __sub__(self, other):
        return ComplexNumber(self.numberRe - other.numberRe, self.numberIm - other.numberIm)

    def __str__(self):
        return str(self.numberRe) + "+" + str(self.numberIm) + "i"
x = ComplexNumber(4,4)
y = ComplexNumber(2,6)
print(x + y)
