from itertools import count
from math import factorial
def genetics():
    for a in count(1):
        yield factorial(a)
genetic = genetics()
x = 0
for i in genetic:
    if x < 25:
        print(i)
        x += 1
    else:
        break


def fast_track(num):
    num_1 = 1
    for i in range(num + 1):
        yield f'{i}! = {num_1}'
        num_1 *= i + 1
for a in fast_track(int(input('номер факториала:  '))):
    print(a)