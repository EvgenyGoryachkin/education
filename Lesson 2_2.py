element_list = list(input("Укажите количество элементов списка "))

for n in range(1, len(element_list), 2):
        element_list[n - 1], element_list[n] = element_list[n], element_list [n - 1]

print(element_list)