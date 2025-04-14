from math import sin, cos, pi
import matplotlib.pyplot as plt


def flower_function(angle, petalas):
    '''
    r(\theta) &= sin(\text{petalas} * \theta) \\
    x(\theta) &= r(\theta) * cos(\theta) \\
    y(\theta) &= r(\theta) * sin(\theta)
    '''
    r = sin(petalas * angle)
    x = r * cos(angle)
    y = r * sin(angle)
    return x, y


angles_radians = [pi * angle / 180 for angle in range(0, 360)]
x_list = []
y_list = []

for angle in angles_radians:
    x, y = flower_function(angle, petalas=4)
    x_list.append(x)
    y_list.append(y)

plt.plot(x_list, y_list, color="pink", linewidth=8, zorder=0)
plt.scatter(0, 0, color="yellow", s=800)

plt.gca().set_aspect(1)
plt.show()
