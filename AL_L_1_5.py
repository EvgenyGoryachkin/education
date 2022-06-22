import numpy as np
import matplotlib.pyplot as plt
title_font = {
    "fontsize": 18,
    "fontweight": "bold",
    "color": "black",
    "family": "serif",
}
legend_font = {
    "size": 14,
    "family": "serif",
}
x = np.linspace(-1, 10)
k1 = 1
k2 = -0.7
plt.figure(figsize = (16, 6))
plt.plot(x,  np.cos(k1*x),label='k1 = 1', linestyle=':', linewidth=4)
plt.plot(x,  np.cos(k2*x),label='k2 = -0.7', linestyle='-', linewidth=4)
plt.xlabel('x')
plt.ylabel('Cos')
plt.title('функция y(k,x)=cos(k∙x)', fontdict=title_font)
plt.legend( prop=legend_font, frameon=False)
plt.show()