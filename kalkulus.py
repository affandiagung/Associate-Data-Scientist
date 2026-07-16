import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400)
y = 2 * x + 1

plt.plot(x, y, label='f(x) = 2x + 1')
plt.title("Linear Function")
plt.legend()
plt.show()