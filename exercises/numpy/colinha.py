import numpy as np


def primeiro_array():
    my_array = np.array([0, 5, 92, 44])
    print(my_array)
    # [0 5 92 44]


def operacoes_escalares():
    my_array = np.array([0, 5, 92, 44])

    print(my_array + 10)  # [ 10  15 102  54]
    print(my_array - 10)  # [-10  -5  82  34]
    print(my_array * 10)  # [  0  50 920 440]
    print(my_array / 10)  # [0.  0.5 9.2 4.4]
    print(my_array // 10)  # [0 0 9 4]
    print(my_array % 10)  # [0 5 2 4]


def operacoes_arrays():
    array_0 = np.array([0, 5, 92, 44])
    array_1 = np.array([10, 20, 30, 40])

    print(array_0 + array_1)  # [ 10  25 122  84]
    print(array_0 - array_1)  # [-10 -15  62   4]
    print(array_0 * array_1)  # [0 100 2760 1760]
    print(array_0 / array_1)  # [0.  0.25  3.06666667 1.1]


def arrays_multidimensionais():
    array_2d = np.array(
        [
            [0, 1],
            [2, 3],
            [4, 5],
        ]
    )

    print(array_2d.T)
    # [[0 2 4]
    #  [1 3 5]]

    print(array_2d[2, 1])  # 5


def array_shapes():
    array_1d = np.array([0, 5, 92, 44])
    print(array_1d.shape)  # (4,)

    array_2d_a = np.array(
        [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1],
        ]
    )
    print(array_2d_a.shape)  # (6, 3)

    array_2d_b = array_2d_a.reshape(2, 9)
    print(array_2d_b.shape)  # (2, 9)


def array_access():
    array_2d = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])

    print(array_2d[2, 1:])
    # [9 10 11]
    print(array_2d[:, 2:])
    # [[2, 3], [6, 7], [10, 11]]

    array_2d[2, 1:] = [-1, -1, -1]
    print(array_2d)
    # [[ 0  1  2  3]
    #  [ 4  5  6  7]
    #  [ 8 -1 -1 -1]]

    array_2d = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])

    mask = [[False, False, True, True], [False, True, False, True], [False, False, False, True]]
    print(array_2d[mask])  # [2 3 5 7]


def matrix_multiplication():
    angle = np.pi / 2
    vector = np.array([1, 0])

    rotation = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])

    print(rotation @ vector)


def operacao_igualdade_errada():
    a = np.array([1, 2, 1, 3, 5])
    b = np.array([1, 2, 1, 0, 5])

    if a == b:
        print("são iguais")
    else:
        print("são diferentes")


def operacao_igualdade():
    a = np.array([1, 2, 1, 3, 5])
    b = np.array([1, 2, 1, 0, 5])

    if np.all(a == b):
        print("são todos iguais")

    elif np.any(a == b):
        print("Algum elemento é igual")

    else:
        print("tá tudo diferente")


def operacoes_logicas():
    a = np.array([False, False, True, True])
    b = np.array([False, True, False, True])

    print(a & b)  # [False False False  True]
    print(a | b)  # [False  True  True  True]
    print(a ^ b)  # [False  True  True False]
    print(~a)  # [ True  True False False]
    print(~b)  # [ True False  True False]

    a = np.array([1, 2, 21, 3, 5, 8, 26])
    mask = (a < 3) | (a > 20)
    a[mask] = 0


def common_functions():
    a = np.array([1, 2, 16, 128, 3])
    np.savetxt("bla.csv", a)

    print(np.radians(a))
    print(np.sin(np.radians(a)))
    print(np.abs(a))
    print(np.round(a, 5))
    print(np.median(a))
    print(np.average(a))
    print(np.loadtxt(a))
    print(np.random.randint(0, 100, size=(4, 5)))
    print(np.random.normal(5, 2, size=(4, 5)))
    print(np.arange(0, 100, 2))
    print(np.linspace(100, 200, 50))
    print()

def fit_function():
    import matplotlib.pyplot as plt

    x = np.linspace(-100, 100, 50)
    y = x ** 3 * 50 - 5 * x ** 2 + 90
    x_ = np.random.normal(x, 5)
    y_ = np.random.normal(y, 1e2)
    np.savetxt("data/cubica_x.csv", x_)
    np.savetxt("data/cubica_y.csv", y_)
    plt.scatter(x_, y_)
    
    poly = np.polyfit(x_, y_, 3)
    plt.plot(x, np.polyval(poly, x))
    plt.show()

    x = np.linspace(0, 10, 50)
    y = -5 * x + 10
    x_ = np.random.normal(x, 0.5)
    y_ = np.random.normal(y, 0.5)
    np.savetxt("data/reta_x.csv", x_)
    np.savetxt("data/reta_y.csv", y_)
    plt.scatter(x_, y_)

    poly = np.polyfit(x_, y_, 1)
    print(poly)

    plt.plot(x, np.polyval(poly, x))
    plt.show()

fit_function()