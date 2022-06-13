class Complex_x:
    def __init__(self, real, a=0):
        self.__complex = complex(real, a)
    def __add__(self, other):
        if isinstance(other, Complex_x):
            other = other.__complex
        complex_ = self.__complex + other
        return Complex_x(complex_.real, int(complex_.imag))
    def __mul__(self, other):
        if isinstance(other, Complex_x):
            other = other.__complex
        complex_ = self.__complex * other
        return Complex_x(complex_.real, int(complex_.imag))
    def __str__(self):
        return self.__complex.__str__()
if __name__ == '__main__':
    c1 = Complex_x(2, -3)
    c2 = Complex_x(5)
    print(c1 + c2, complex(8, -4) + complex(25))
    print(c1 * c2, complex(8, -4) * complex(25))
