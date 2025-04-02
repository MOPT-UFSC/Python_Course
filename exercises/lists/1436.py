n = int(input())

for i in range(n):
    valores = input().split()
    qt = int(valores[0])
    lista = list()
    for j in range(qt):
        lista.append(int(valores[j + 1]))
    print(f'Case {i+1}: {lista[qt // 2]}')