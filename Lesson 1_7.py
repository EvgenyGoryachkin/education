while True:
    total_days = 1
    a = float(input("Укажите количество км за первый день "))
    b = float(input("Укажите планируемый результат тренировки в км "))
    if a < 0 or b < 0:
        print("значения должны быть больше 0")
    else:
        while a < b:
            a += a * 0.1
            total_days += 1
        print(f"План будет достигнут через {total_days: .0f} дня (-ей)")
        break