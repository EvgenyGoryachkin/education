
class DivisionZero(Exception):
    a = "Деление на ноль запрещено"
    def __str__(self):
        return self.a
class Number(float):
    def __truediv__(self, unit):
        if unit is not None and not unit:
            raise DivisionZero
        return Number(float(self) / float(unit))
if __name__ == '__main__':
    while True:
        try:
            dividend, divider = map(Number, input("Введите делимое и делитель через пробел: ").split())
            print(dividend / divider)
        except DivisionZero as z:
            print(z)
        except ValueError as z:
            print(z)
        break