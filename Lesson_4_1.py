def amount():
    try:
        time = float(input('Выработка в часах -  '))
        salary = int(input('Сумма ставки -  '))
        bonus = int(input('Сумма премиии -  '))
        summery = time * salary + bonus
        print(f'Заработная плата сотрудника  {summery}')
    except ValueError:
        return print('Не число')
amount()

