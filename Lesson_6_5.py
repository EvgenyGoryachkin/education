class Stationary:
    def __init__(self, title=' - отрисовка возможна - '):
        self.title = title
    def draw(self):
        print(f'Начинайте отрисовку {self.title}')
class Pen(Stationary):
    def draw(self):
        print(f'Начините писать с {self.title} !')
class Pencil(Stationary):
    def draw(self):
        print(f'Начините писать с {self.title} !')
class Handle(Stationary):
    def draw(self):
        print(f'Начините писать с {self.title} !')
x = Stationary()
pen = Pen('Ручкой')
pencil = Pencil('Карандашом')
handle = Handle('Фломастером')
office = [x, pen, pencil, handle]
for i in office:
    i.draw()
