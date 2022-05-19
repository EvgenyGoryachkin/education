def number ():
    x = 0
    while True:
        list_1 = input('ВВедите последовательность значений через пробел или для выхода Q - ').split()
        for a in list_1:
            if a.lower() == "q":
                return x
            else:
                try:
                    x +=int(a)
                except ValueError:
                    print("Для выхода нажмите 'Q' ")

        print(f"Финальная сумма- {x}")

print(number())