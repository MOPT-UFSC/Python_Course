import numpy as np
import sys


n = int(sys.argv[1])
m1 = np.random.randint(0, 100, size=(n, n))
m2 = np.random.randint(0, 100, size=(n, n))
result = m1 @ m2
