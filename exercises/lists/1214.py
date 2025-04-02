c = int(input())

for i in range(c):
    valores = list(map(int, input().split()))

    somatorio = 0.0
    for j in range(1, valores[0]+1):
        somatorio += valores[j]
    
    media = somatorio / float(valores[0])

    somatorio = 0.0
    for j in range(1, valores[0]+1):
        if float(valores[j]) >= media:
            somatorio += 1
    print(f'{((somatorio / float(valores[0])) * 100.0):.3f}%')
    