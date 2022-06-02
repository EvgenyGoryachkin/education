from functools import reduce
def x_func(d_p, d):
    return d_p * d
print(f'Список {[d for d in range(99, 1001) if d % 2 == 0]}')
print(f'Итог после перемножения  {reduce(x_func, [d for d in range(99, 1001) if d % 2 == 0])}')
