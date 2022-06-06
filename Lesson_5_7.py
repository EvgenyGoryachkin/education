import json
plus_x = {}
y = {}
count = 0
count_prof = 0
i = 0
with open('Ver_5_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        plus_x[name] = int(earning) - int(damage)
        if plus_x.setdefault(name) >= 0:
            count = count + plus_x.setdefault(name)
            i += 1
    if i != 0:
        count_prof = count / i
        print(f'Прибыль средняя - {count_prof:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    y = {'средняя прибыль': round(count_prof)}
    plus_x.update(y)
    print(f'Прибыль каждой компании - {plus_x}')

with open('Ver_5_7_1.json', 'w') as table_js:
    json.dump(plus_x, table_js)

    str = json.dumps(plus_x)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {str}')