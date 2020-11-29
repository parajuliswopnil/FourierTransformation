import matplotlib.pyplot as plt
import math
import numpy as np
from itertools import count
from matplotlib.animation import FuncAnimation

frequency = 1
n = 1
count = count(1)
t = np.arange(0, 1, 0.001)
Y = []
j = 0


def sine_adder(n):
    if n == 0:
        return 0
    else:
        while n >= 0:
            return math.sin(2 * math.pi * t[i] * frequency * (2 * n - 1)) / (2 * n - 1) + sine_adder(n - 1)


while n < 15:
    n = next(count)
    for i in range(0, len(t)):
        y = sine_adder(n)
        Y.append(y)
    plt.plot(t, Y)
    plt.show()
    Y.clear()

plt.tight_layout()
