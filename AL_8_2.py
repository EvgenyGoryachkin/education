import numpy as np
np.warnings.filterwarnings('ignore')
A = np.array([[1, 2, -1],
             [3, -4, 0],
             [8, -5, 2],
             [2, 0, -5],
             [11, 4, -7]])
B = np.array([1, 7, 12, 7, 15])
X = np.linalg.lstsq(A, B)
print(X)