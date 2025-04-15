import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def create_fit_function():
    x = np.linspace(-100, 100, 50)
    y = x**3 * 50 - 5 * x**2 + 90
    x_ = np.random.normal(x, 5)
    y_ = np.random.normal(y, 1e2)
    np.savetxt("data/cubica_x.csv", x_)
    np.savetxt("data/cubica_y.csv", y_)
    plt.scatter(x_, y_)
    plt.show()

    x = np.linspace(0, 10, 50)
    y = -5 * x + 10
    x_ = np.random.normal(x, 0.5)
    y_ = np.random.normal(y, 0.5)
    np.savetxt("data/reta_x.csv", x_)
    np.savetxt("data/reta_y.csv", y_)
    plt.scatter(x_, y_)
    plt.show()

    x = np.linspace(0, np.pi * 2, 100)
    y = 2 * np.sin(x * 2 + np.pi / 4)
    x_ = np.random.normal(x, 0.05)
    y_ = np.random.normal(y, 0.05)
    np.savetxt("data/sin_x.csv", x_)
    np.savetxt("data/sin_y.csv", y_)
    plt.scatter(x_, y_)
    plt.show()


def fit_linear():
    def f(x, a, b):
        return a * x + b

    data_x = np.loadtxt("data/reta_x.csv")
    data_y = np.loadtxt("data/reta_y.csv")

    (a, b), pcov = curve_fit(f, data_x, data_y)
    print(a, b)

    plt.scatter(data_x, data_y)
    plt.plot(data_x, f(data_x, a, b))
    plt.show()


def fit_cubic():
    def g(x, a, b, c, d):
        return a * x**3 + b * x**2 + c * x + d

    data_x = np.loadtxt("data/cubica_x.csv")
    data_y = np.loadtxt("data/cubica_y.csv")

    args, pcov = curve_fit(g, data_x, data_y)
    print(args)

    plt.scatter(data_x, data_y)
    plt.plot(data_x, g(data_x, *args))
    plt.show()


def fit_sin():
    def g(x, amplitude, frequency, phase):
        return amplitude * np.sin(x * frequency + phase)

    data_x = np.loadtxt("data/sin_x.csv")
    data_y = np.loadtxt("data/sin_y.csv")

    (amplitude, frequency, phase), pcov = curve_fit(g, data_x, data_y)

    plt.scatter(data_x, data_y)
    plt.plot(data_x, g(data_x, amplitude, frequency, phase))
    plt.show()


def create_signal():
    duration = 10  # sec
    sample_rate = 50  # Hz

    x = np.linspace(
        0,
        duration,
        duration * sample_rate,
        endpoint=False,
    )
    y = 2 * np.sin(x * 2 * np.pi) + np.sin(20 * x * 2 * np.pi)
    np.savetxt("data/signal.csv", y)

    plt.plot(x, y)
    plt.show()


def test_fft():
    from scipy.fft import fft, fftfreq

    sample_rate = 50  # Hz
    signal = np.loadtxt("data/signal.csv")

    xf = fftfreq(len(signal), 1 / sample_rate)
    yf = fft(signal)

    plt.stem(xf, np.abs(yf))
    plt.axvline(x=0, color="black", linestyle="dashed")
    plt.show()


def test_filter():
    from scipy.signal import butter, filtfilt

    sample_rate = 50  # Hz
    signal = np.loadtxt("data/signal.csv")

    cutting_frequency = 20 / sample_rate
    b, a = butter(4, cutting_frequency, btype='lowpass')

    filtered_data = filtfilt(b, a, signal)

    plt.plot(filtered_data)
    plt.show()


def dense_matrix():
    n = 10_000 * 3
    dense = np.zeros((n, n), dtype=complex)

    i = np.arange(n)
    j = np.arange(n)
    dense[i, j] = 12

    i = np.arange(0, n-1)
    j = np.arange(1, n)
    dense[i, j] = 18

    i = np.arange(1, n)
    j = np.arange(0, n-1)
    dense[i, j] = 35

    dense @ dense.T

def sparse_matrix():
    from scipy.linalg import det
    from scipy.sparse import csr_matrix, csc_matrix, lil_matrix, dok_matrix
    
    n = 10_000 * 3
    dense = lil_matrix((n, n), dtype=complex)

    i = np.arange(n)
    j = np.arange(n)
    dense[i, j] = 12

    i = np.arange(0, n-1)
    j = np.arange(1, n)
    dense[i, j] = 18

    i = np.arange(1, n)
    j = np.arange(0, n-1)
    dense[i, j] = 35

    result = dense @ dense.T
    print()

sparse_matrix()

# print(dense @ dense.T)

# create_fit_function()
# fit_linear()
# fit_cubic()
# fit_sin()

# create_signal()
# test_fft()

# test_filter()