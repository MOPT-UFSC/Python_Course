from math import sin, cos, pi
import matplotlib.pyplot as plt


'''
x(\theta) &= cos(\theta) \\
y(\theta) &= sin(\theta) \\
z(\theta) &= \theta
'''

angles_radians = [pi * angle / 180 for angle in range(0, 360 * 3)]
x_list = [cos(a) for a in angles_radians]
y_list = [sin(a) for a in angles_radians]
z_list = [a for a in angles_radians]

plt.subplots(subplot_kw={"projection": "3d"})

plt.plot(x_list, y_list, z_list, linewidth=10, color="green")
plt.show()