from time import sleep
class Light:
    __color = ['Красный', 'Желтый', 'Зеленый']
    def running(self):
        i = 0
        while i < 3:
            print(f'Внимание! смена сигнала светофора  \n '
                  f'{Light.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1
Light = Light()
Light.running()