from math import sqrt, sin
import matplotlib.pyplot as plt


def heart(x):
    k = 50
    part_1 = (x**2) ** (1 / 3)
    part_2 = 0.7 * sin(k * x) * sqrt(3 - x**2)
    return part_1 + part_2


x = [i / 100 for i in range(-170, 170)]
y = [heart(x_) for x_ in x]

plt.plot(x, y, color="red", linewidth=5)
plt.show()
