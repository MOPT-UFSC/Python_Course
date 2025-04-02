n = int(input())
contador = dict()

for _ in range(n):
    val = int(input())

    if val not in contador:
        contador[val] = 0

    contador[val] += 1

for numero, frequencia in sorted(contador.items()):
    print(f"{numero} aparece {frequencia} vez(es)")