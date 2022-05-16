def nitro(x, y):
    number = 1
    for i in range(abs(y)):
       number *= x
    if y >= 0:
        return number
    else:
        return 1 / number
print(nitro(float(input("Первое значение - ")), int(input("Второе значение - "))))

def nitro_1(x, y):
   numbers_1 = x ** y
   return numbers_1
print(nitro_1(float(input("Первое значение - ")), int(input("Второе значение - "))))