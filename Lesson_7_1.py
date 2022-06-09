import copy
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            s = s + '\t'.join(map(str,self.matrix[i])) + '\n'
        return s
    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        res = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                res[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(res)
a = [[5, 3, 1, 6],[4, 4, 4, 5],[-9, 0, 6, 0]]
b = [[11, 21, 41, 51],[31, 41, 51, 61],[51, 51, 61, 61]]
m = Matrix(a)
s = Matrix(b)
print(m)
summ = m + s
print('summ ')
print(summ)
print(type(summ))