import matplotlib.pyplot as plt


def example_0():
    plt.plot([0, 1, 2, 3, 4])
    plt.show()


def example_1():
    plt.plot([0, 1, 2, 3, 4])
    plt.plot([0, 2, 4, 6, 8])
    plt.show()


def example_2():
    plt.plot([0, 1, 2, 3])
    plt.plot([0, 10, 20, 30], [0, 1, 2, 3])
    plt.show()


def example_3():
    x = [10, 20, 30, 40]
    y0 = [1, 2, 4, 8]
    y1 = [2, 3, 5, 9]
    y2 = [3, 4, 6, 10]
    y3 = [4, 5, 7, 11]

    plt.plot(x, y0, color="red", linestyle="dashed")
    plt.plot(x, y1, color="green", linestyle="dotted")
    plt.plot(x, y2, color="blue", linestyle="dashdot")

    plt.plot(
        x,
        y3,
        color="black",
        linestyle=(0, (5, 1, 5, 3, 1, 3)),
    )

    plt.show()


def example_4():
    x = [10, 20, 30, 40]
    y1 = [1, 2, 4, 8]
    y2 = [2, 3, 5, 9]
    y3 = [3, 4, 6, 10]

    plt.plot(x, y1, color="red", marker="o")
    plt.plot(x, y2, color="green", marker="+")
    plt.plot(x, y3, color="blue", marker="v")
    plt.show()


def example_5():
    x0 = list(range(100))
    y1 = [(x**2) for x in x0]
    y2 = [(x * 80) for x in x0]

    plt.plot(x0, y1, color="red", marker="o", markevery=10)
    plt.plot(x0, y2, color="green", marker="+", markevery=20)
    plt.show()


def example_6():
    x0 = list(range(100))
    y1 = [(x**2) for x in x0]
    y2 = [(x * 80) for x in x0]

    plt.plot(
        x0,
        y1,
        color="red",
        marker="o",
        markevery=[0, 36, -1],
    )

    plt.plot(
        x0,
        y2,
        color="green",
        marker="+",
        markevery=slice(40, 50, 2),
    )

    plt.show()


def example_7():
    from random import normalvariate

    x0 = list(range(100))
    y0 = [normalvariate(x, 10) for x in x0]
    y1 = x0

    plt.scatter(x0, y0, color="red", marker="+", s=10)
    plt.plot(x0, y1, color="green", linewidth=5, zorder=0)
    plt.show()


def example_8():
    x = ["peras", "maçãs", "laranjas"]
    y = [20, 10, 30]
    plt.bar(x, y, color=["green", "red", "orange"])
    plt.show()


def example_9():
    from random import randint

    x0 = list(range(100))
    y0 = [(x**2) for x in x0]
    y_min = [(x - randint(5, 10)) ** 2 for x in x0]
    y_max = [(x + randint(5, 10)) ** 2 for x in x0]

    plt.plot(x0, y0, color="red")
    plt.fill_between(x0, y_min, y_max, color="green", alpha=0.5)
    plt.show()


def example_10():
    matrix = []
    for y in range(-100, 100):
        line = []
        for x in range(-100, 100):
            val = x * x - y * y
            line.append(val)
        matrix.append(line)

    plt.imshow(matrix, cmap="magma")
    plt.show()


def example_11():
    matrix = []
    for y in range(-100, 100):
        line = []
        for x in range(-100, 100):
            val = x * x - y * y
            line.append(val)
        matrix.append(line)

    plt.gca().set_aspect(1)
    plt.contour(matrix)
    # plt.contourf(matrix)
    plt.show()


def example_12():
    x0 = range(-100, 100, 10)
    y0 = range(-100, 100, 10)
    U = []
    V = []

    for y in y0:
        u_line = []
        v_line = []

        for x in x0:
            u_line.append(x + y)
            v_line.append(x - y)

        U.append(u_line)
        V.append(v_line)

    plt.quiver(x0, y0, U, V)
    plt.show()


def example_13():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    z = [1, 4, 9, 16, 25]

    plt.subplots(subplot_kw={"projection": "3d"})

    plt.plot(x, y, z)
    plt.show()


def example_14():
    from math import sqrt
    from random import normalvariate

    def func(x):
        return sqrt(2**x) / 5

    x0 = list(range(100))
    y0 = [func(x) for x in x0]
    y1 = [func(normalvariate(x, 10)) for x in x0]

    plt.plot(x0, y0, color="blue", label=r"$f(x) = \frac{\sqrt{2^x}}{5}$")
    plt.scatter(x0, y1, color="red", marker="+", s=10, label="Acquired data")

    plt.title("My weird data fitting")
    plt.xlabel("Numbers from 0 to 100")
    plt.ylabel("Whatever values")

    plt.yscale("log")
    plt.legend()
    plt.show()


def example_15():
    fig, ax = plt.subplots(2, 2, sharey=True)

    ax[0][0].plot([1, 2, 3, 4], color="red")
    ax[0][1].plot([2, 4, 6, 8], color="green")
    ax[1][0].plot([3, 6, 9, 12], color="blue")
    ax[1][1].plot([4, 8, 12, 16], color="black")

    plt.show()
