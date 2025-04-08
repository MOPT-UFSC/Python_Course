from random import randint, seed
from time import time

seed(0)
conjunto = set()
size = 10_000_000
cont = 0

inicio = time()
for i in range(size):
    n = randint(0, size)
    if n in conjunto:
        cont += 1
    else:
        conjunto.add(n)
final = time()

print(f'tempo: {final - inicio}')
print(f'{cont=}')
print(f'{size - cont = }')
print(f'{(size - cont) / cont = }')