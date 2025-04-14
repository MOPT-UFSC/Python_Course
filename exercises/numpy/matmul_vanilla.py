from random import randint
import sys


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


n = int(sys.argv[1])
m1 = random_matrix(n)
m2 = random_matrix(n)
result = matmul(m1, m2)
