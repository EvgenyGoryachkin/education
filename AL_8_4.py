import numpy as np
np.warnings.filterwarnings('ignore')
A = np.array([[1, 2, 3],
             [2, 16, 21],
             [4, 28, 73]])
import scipy
import scipy.linalg
P, L, U = scipy.linalg.lu(A)
print(P)
print(L)
print(U)