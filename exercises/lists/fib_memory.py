termo_1 = 0
termo_2 = 1
aux = 0
memoria: list[int] = list()

while True:
    n = int(input("Digite um número (0 para sair): "))
    if n == 0:
        break
    
    if n <= len(memoria):
        print(memoria[n])
    else:
        for i in range(n):
            memoria.append(termo_1)
            aux = termo_1
            termo_1 = termo_2
            termo_2 = aux + termo_1
        
        memoria.append(termo_1)
        print(termo_1)