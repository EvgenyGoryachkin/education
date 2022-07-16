import numpy as np
np.warnings.filterwarnings('ignore')
A = np.array([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])
B = np.array([2, 5, 11])
c = np.linalg.lstsq(A, B)
print(c)
