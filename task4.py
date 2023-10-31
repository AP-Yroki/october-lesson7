import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = 6 * x - 2

plt.plot(x, y, label='y = 6x - 2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График линейной функции y = 6x - 2')
plt.grid(True)
plt.legend()
plt.show()