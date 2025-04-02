linha_escolhida = int(input())
operacao = input()

matriz = list()

for i in range(12):
    linha = list()
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0.0
for i in range(12):
    soma += matriz[linha_escolhida][i]

if operacao == "S":
    print(soma)
else:
    print(soma / 12.0)
