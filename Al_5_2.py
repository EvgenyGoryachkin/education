import numpy as np
k = 0
m = 0
pk = 0.5
pm = 0.5
for i in range(1):
    np.random.uniform(0, 10)
    if i > 5:
        k += 1
    else:
        m += 1
if (pk + pm) == k or (pk + pm) == m:
    print('результат - или oрел или решка')

    