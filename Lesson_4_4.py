my_roll_basic = [23, 1, 4, 4, 2, 3, 2, 8, 8, 10, 8, 5, 11, 44, 44]
my_roll = [x for x in my_roll_basic if my_roll_basic.count(x) == 1]
print(my_roll)