import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.animation import FuncAnimation
frequency = 5
n = 60
t = np.arange(0, 1, 0.001)
Y = []

def sine_adder(n):
    if n == 0:
        return 0
    else:
        while n >= 0:
            return math.sin(2 * math.pi * t[i] * frequency * (2 * n - 1)) / (2 * n -1) + sine_adder(n - 1)


for i in range(0, len(t)):
        y = sine_adder(n)
        Y.append(y)


plt.plot(t, Y)

plt.tight_layout()
plt.show()

