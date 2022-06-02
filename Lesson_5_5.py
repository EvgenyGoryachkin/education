def summary():
    try:
        with open('Ver_5_5.txt', mode='w+', encoding="utf-8") as file_txt:
            line = input('Введите цифры через пробел \n')
            file_txt.writelines(line)
            number_x = line.split()

            print(sum(map(int, number_x)))
    except IOError:
        print('Ошибка в хранилище')
    except ValueError:
        print('Неправильно набран номер.')
summary()