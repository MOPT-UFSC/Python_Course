n = int(input())

campo = list()
for i in range(n):
    campo.append(int(input()))

mapeado = list()

if len(campo) == 1:
    print(campo[i])
else:
    for i in range(n):
        if i == 0:
            print(campo[i] + campo[i+1])
        elif i == n-1:
            print(campo[i-1] + campo[i])
        else:
            print(campo[i-1] + campo[i] + campo[i+1])
