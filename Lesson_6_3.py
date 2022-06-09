class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def full_name(self):
        return self.name + ' ' + self.surname
    def total_income(self):
        return self._income.get('wage') + self._income.get('bonus')
count = Position('Иван', 'Федорович', 'и.о. начальника отдела', 10000, 50000)
print(count.full_name())
print(count.position)
print(count.total_income())