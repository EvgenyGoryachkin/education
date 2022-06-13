class Number(int):
    def __str__(self):
        return f"{self:02}"
class Date:
    date_unit = ('day', 'month', 'year')
    def __init__(self, date: str, /):
        day, month, year = self.transform(date.split('-'))
        if not self.validate(day, month, year):
            raise ValueError(f"{date} Неправильный формат даты")
        self.day = day
        self.month = month
        self.year = year
    def __iter__(self):
        for attr in self.date_unit:
            yield self.__getattribute__(attr)
    @classmethod
    def transform(cls, date):
        return [Number(p) for p in date]
    @staticmethod
    def validate(*date):
        if not all(map(lambda z: isinstance(z, int), date)):
            return False
        day, month, year = date
        return all([1 <= day <= 31, 1 <= month <= 12, year >= 1900])
    def __str__(self):
        return f"Дата '{'-'.join([str(s) for s in self])}'"
if __name__ == '__main__':
    try:
        print(Date('12-06-2022'))
        print(Date('01-12-1969'))
        print(Date('12-24-1915'))
    except ValueError as e:
        print(e)