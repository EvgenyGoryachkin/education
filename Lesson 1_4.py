n = abs(int(input("Укажите значение параметра, целое положительное число ")))
maximum = n % 10
while n >=1:
    n = n // 10
    if n % 10 > maximum:
        maximum = n % 10
    else:
        print("Максимальная цифра в числе   ", maximum)
        break


