import numpy as np
np.warnings.filterwarnings('ignore')
A = np.array([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])
B = np.array([[12, 2, 1]])
C = np.concatenate((A, B.T), axis=1)
print(C)
C_1 = np.linalg.matrix_rank(A, 0.0001), np.linalg.matrix_rank(C, 0.0001)
print(C_1)
B = np.array([12, 2, 3])
D = np.linalg.solve(A, B)
print(D)
# решений нет в связи с тем, что основная матрица мкеньше расширенной матрицы.