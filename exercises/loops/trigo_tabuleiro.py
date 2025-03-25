c = int(input())
for j in range(c):
    n = int(input())
    
    qtGraos = 1
    for i in range(n):
        qtGraos *= 2
    print(f'{int(qtGraos / 12000)} kg')