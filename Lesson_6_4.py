class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'{self.name} Движение'
    def stop(self):
        return f'{self.name} Остановка'
    def turn_right(self):
        return f'{self.name} Поворот на право'
    def turn_left(self):
        return f'{self.name} Поворот на лево'
    def show_speed(self):
        return f'Текущая скорость {self.name}  -  {self.speed}'
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name}  -  {self.speed}')
        if self.speed > 40:
            return f'Скорость {self.name} выше скорости городского автомобиля'
        else:
            return f'Скорость {self.name} нормальная для городского автомобиля'
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Текущая скорость грузового транспорта {self.name}  - {self.speed}')
        if self.speed > 60:
            return f'Скорость {self.name} выше разрешенной для грузового транспорта'
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def police(self):
        if self.is_police:
            return f'{self.name} из департамента полиции'
        else:
            return f'{self.name}не из департамента полиции'
a = SportCar(200, 'Красный', 'Mersedes', False)
b = TownCar(49, 'Белый', 'Ниссан', False)
c = WorkCar(65, 'Оранжевый', 'УАЗ', True)
d = PoliceCar(150, 'Темно-синий',  'Лада', True)
print(c.turn_left())
print(f'Когда {b.turn_right()}, значит {a.stop()}')
print(f'{c.go()}  с уточненной скоростью {c.show_speed()}')
print(f'{c.name}  -  {c.color}')
print(f'{a.name} специальная машина (полицейская)? {a.is_police}')
print(f' {c.name}  специальная машина (полицейская)? {c.is_police}')
print(a.show_speed())
print(b.show_speed())
print(d.police())
print(d.show_speed())