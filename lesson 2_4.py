Line_1 = input("Введите набор слов ")
Line_1_list = []
x = 1
for s in range(Line_1.count(' ') + 1):
    Line_1_list = Line_1.split()
    if len(str(Line_1_list)) <= 10:
        print(f" {x} {Line_1_list [s]}")
        x += 1
    else:
        print(f" {x} {Line_1_list [s] [0:10]}")
        x += 1