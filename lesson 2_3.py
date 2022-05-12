month = int(input("Введите месяц по номеру "))
seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {'winter': [12, 1, 2], 'spring': [3, 4, 5], 'summer': [6,7,8], 'autumn': [9, 10,11]}

if month < 0 or month > 12:
    print("Такого месяца не существует")
if month in sum(seasons_dict.values(), []):
    for n in seasons_dict.items():
        if month in n[1]:
            print(n[0])
            break