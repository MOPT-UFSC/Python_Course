while True:
    n = int(input())
    if n == 0:
        break
    valores = input().split()
    for i in range(n):
        valores[i] = int(valores[i])
    
    maria = 0
    joao = 0
    for i in range(n):
        if valores[i] == 0:
            maria += 1
        else:
            joao += 1
    print(f'Mary won {maria} times and John won {joao} times')