exercise = open('test.txt', 'w')
line = input('Введите текст \n')
while line:
    exercise.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

exercise.close()
exercise = open('test.txt', 'r')
content = exercise.readlines()
print(content)
exercise.close()