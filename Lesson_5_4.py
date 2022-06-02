dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять"}
with open("Ver_5_4_1.txt", "w", encoding="utf-8") as n_list:
    with open('Ver_5_4.txt', encoding='utf-8') as o_list:
        n_list.writelines([line.replace(line.split()[0], dictionary.get(line.split()[0])) for line in o_list])
        