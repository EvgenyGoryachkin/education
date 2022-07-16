import numpy as np
np.warnings.filterwarnings('ignore')
A = np.array([[1, 2, -1],
             [8, -5, 2]])
B = np.array([1, 12])
import matplotlib.pyplot as plt
def Q(x, y, z):
    return x**2 + y**2 + z**2
x = np.linspace(-1, 10, 200)
c = np.linalg.lstsq(A, B)
print(c)
