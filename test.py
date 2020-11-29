import matplotlib.pyplot as plt
import math
import numpy as np
from itertools import count
from matplotlib.animation import FuncAnimation

frequency = 1
t = np.arange(0, 1, 0.001)
n = 1
count1 = count(1)
Y = []
j = 0
i = 0
fig = plt.figure()

def sine_adder(n):
    if n == 0:
        return 0
    else:
        while n >= 0:
            return math.sin(2 * math.pi * t[i] * frequency * (2 * n - 1)) / (2 * n - 1) + sine_adder(n - 1)


def animate(y):
    Y.append(y)

while n < 15:
    n = next(count1)
    for i in range(0, len(t)):
        y = sine_adder(n)
        animate(y)
    plt.plot(t, Y)
    plt.show()
    Y.clear()

ani = FuncAnimation(fig, animate, interval=2000)

plt.tight_layout()

