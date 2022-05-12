roster = [9, 6, 4, 2]
number = ""

while number != "f":
    s = 0
    number = input("Укажите число  . Завершить - f")
    if number.isdigit():
        for x in roster:
            if int(number) <= x:
                s += 1
            else:
                break
        roster.insert(s, int(number))
    print(roster)
