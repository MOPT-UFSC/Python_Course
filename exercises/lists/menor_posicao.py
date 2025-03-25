n = int(input())

lista = list(map(int, input().split()))

menor = lista[0]
posicao = 0
for i in range(n):
    if menor > lista[i]:
        menor = lista[i]
        posicao = i
print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')