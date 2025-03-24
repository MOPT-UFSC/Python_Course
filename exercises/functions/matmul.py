import numpy as np
from random import randint, seed
from time import time
from pprint import pprint


def random_matrix(n):
    return [[randint(0, 100) for _ in range(n)] for _ in range(n)]


def zero_matrix(n):
    return [[0 for _ in range(n)] for _ in range(n)]


def matmul(m1, m2):
    size = len(m1)
    result = zero_matrix(size)

    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

n = 1000
a = random_matrix(n)
b = random_matrix(n)

start = time()
x = matmul(a, b)
end = time()
print("Python time", end - start)

start = time()
y = np.matmul(a, b)
end = time()
print("Numpy time", end - start)
