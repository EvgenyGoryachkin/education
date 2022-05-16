def int_func(*args):
    s = input("Внесите необходимые слова ")
    print(s.title())
    return
int_func()

def int_func_1(s):
    eng = "abcdefghijklmnopqrstuvwxyz"
    return s.title() if not set(s).difference(eng) else False
    s = input("Внесите необходимые слова с использованием латинских символов ").split()
int_func()