while True:
    n = int(input())
    if n == 0:
        break
    
    valores = input().split()
    
    maria, joao = 0, 0
    for i in range(n):
        if int(valores[i]):
            joao += 1
        else:
            maria += 1
    print(f'Mary won {maria} times and John won {joao} times')