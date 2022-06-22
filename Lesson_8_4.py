class Store:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year
    def action(self):
        return 'Не определено'
    def __str__(self):
        return f'{self.name} {self.make} {self.year}'
class Printer(Store):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series
    def __str__(self):
        return f'{self.name} {self.series} {self.make} {self.year}'
    def action(self):
        return 'Для печати'
class Scaner(Store):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)
    def action(self):
        return 'Для сканирования'
class Xerox(Store):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)
    def action(self):
        return 'Для копирования'
warhouse = []
scaner = Scaner('Canon','Extra 4504CU', 2009)
warhouse.append(scaner)
xerox = Xerox('Epson','LT 8012', 2015)
warhouse.append(xerox)
printer = Printer("320000",'Matrix', 'Ultra', 2002)
warhouse.append(printer)
print("На складе имеются:")
for x in warhouse:
    print(x,end=' ')
    print(x.action())
for x in warhouse:
    if isinstance(x,Printer):
        warhouse.remove(x)
print("\nНа складе осталось:")
for x in warhouse:
 print(x,end=' ')
 print(x.action()) 