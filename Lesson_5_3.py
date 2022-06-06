with open('Ver_5_3.txt', 'r', encoding='utf-8') as my_text:
    rich = []
    cheap = []
    my_list = my_text.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000.00:
           cheap.append(i[0])
        rich.append(i[1])
print(f'Оклад меньше 20 тыс {cheap}, средний оклад {sum(map(int, rich)) / len(rich)}')