with open('Ver_5_2.txt', encoding='utf-8') as f:
    exercise = f.readlines()
    for index, value in enumerate(exercise,1):
        words = len(value.split())
        print(f'Строчка {index} содержит {words} слов')
        