my_schedule = [15, 16, 2, 3, 1, 7, 5, 4, 10]
my_schedule_a = [x for number, x in enumerate(my_schedule) if my_schedule[number - 1] < my_schedule[number]]
print(f'Исходный список {my_schedule}')
print(f'Новый список {my_schedule_a}')