import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y1 = 6 * x**3 - 2 * x + 8
y2 = 3 * x + 1

plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.plot(x, y1)
plt.title('F(x, y) = 6x^3 - 2x + 8')

plt.subplot(122)
plt.plot(x, y2)
plt.title('F(x, y) = 3x + 1')

plt.show()
