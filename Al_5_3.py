import numpy as np
x0 = np.random.randn(10)
x1 = np.random.randn(10)
x2 = np.random.randn(10)
x3 = np.random.randn(10)
x4 = np.random.randn(10)
x5 = np.random.randn(10)
x6 = np.random.randn(10)
x7 = np.random.randn(10)
x8 = np.random.randn(10)
x9 = np.random.randn(10)
x_sum = x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9
x_sum
import matplotlib.pyplot as plt
plt.hist(x_sum)
plt.show()