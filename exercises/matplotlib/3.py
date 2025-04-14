from math import sin, cos, pi
import matplotlib.pyplot as plt


def lissajous(angle, a, b):
    '''
    x(\theta) &= sin(a * \theta) \\
    y(\theta) &= cos(b * \theta)
    '''
    x = sin(a * angle)
    y = cos(b * angle)
    return x, y


angles_radians = [pi * angle / 180 for angle in range(0, 361, 5)]
num_frequencies = 4

fig, ax = plt.subplots(num_frequencies, num_frequencies)

for a in range(num_frequencies):
    for b in range(num_frequencies):
        x_list = []
        y_list = []

        for angle in angles_radians:
            x, y = lissajous(angle, a + 1, b + 1)
            x_list.append(x)
            y_list.append(y)

        ax[a][b].plot(x_list, y_list, color="black")
        ax[a][b].set_title(f"{a+1}:{b+1}")
        ax[a][b].set_xticklabels([])
        ax[a][b].set_yticklabels([])
        ax[a][b].set_aspect(1)

plt.subplots_adjust(hspace=0.5)
plt.savefig("lissajous.png")
plt.show()
