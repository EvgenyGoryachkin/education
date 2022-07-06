import numpy as np
k = 0
n = 1000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1
print(k, n, k/n)

P = 6 / 2**4
print(P)

k = 0
n = 1000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
e = np.random.randint(0, 2, n)
x = a + b + c + d + e
for i in range(0, n):
    if x[i] == 3:
        k = k + 1
print(k, n, k/n)

C_N = 5*4*3*2 / (3*2*2)
P_N = C_N / 2**5
print(P_N)