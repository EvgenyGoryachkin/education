class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)
    def __str__(self):
        return f'Итог задания {self.quantity * "*"}'
    def __add__(self, other):
        return Cell(self.quantity + other.quantity)
    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Значение отрицательное')
    def __mul__(self, other):
      return Cell(int(self.quantity * other.quantity))
    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))
    def make_order(self, cells_x):
        x = ''
        for i in range(int(self.quantity / cells_x)):
            x += f'{"*" * cells_x} \\n'
        x += f'{"*" * (self.quantity % cells_x)}'
        return x
cells1 = Cell(56)
cells2 = Cell(37)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(8))
print(cells1.make_order(16))
print(cells1 / cells2)