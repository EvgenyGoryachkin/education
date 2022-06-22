class NumberOnly(Exception):
    def __init__(self, a):
        self.a = a
    def __str__(self):
        return self.a
if __name__ == '__main__':
    list_z = []
    while True:
        d = input("Введите число, или 'пробел' для выхода: ")
        if d == " ":
            break
        try:
            if not d.isdigit():
                raise NumberOnly(f"'{d}' не число")
            list_z.append(int(d))
        except NumberOnly as e:
            print(e)
    print(list_z)