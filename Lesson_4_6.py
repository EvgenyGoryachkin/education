from itertools import count
from itertools import cycle
summery_1 = count(1)
summery_2 = cycle('ABCDEF')
for _ in range(20):
    print('(Значение_1, Значение_2) - ({}, {})'.format(next(summery_1), next(summery_2)))

