import matplotlib.pyplot as plt
import numpy as np

x = np.array ([0, 1, 2, 3, 4])
f = 3 * x + 1
plt.plot(f, 'r--', color= 'red', label = 'f(x) = 3x + 1')

plt.legend()
plt.show()