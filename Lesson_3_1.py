def div(*args):
    try:
        arg1 = int(input("Укажите 1-е число "))
        arg2 = int(input("Укажите 2-е число "))
        res = arg1 / arg2
    except ValueError:
        return 'Ошибка значения'
    except ZeroDivisionError:
        return "Деление на ноль! Второе число всегда больше 0"
    return round(res, 4)
print(f'result  {div()}')