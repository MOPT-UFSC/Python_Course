while True:
    n = int(input())
    if n == 0:
        break
    
    nome_ass: dict[str, str] = dict()
    for i in range(n):
        entrada = input().split()
        nome_ass[entrada[0]] = entrada[1]
    
    presentes = int(input())
    ass_falsas = 0
    for i in range(presentes):
        entrada = input().split()
        qt_letras_erradas = 0
        for j in range(len(entrada[1])):
            if nome_ass[entrada[0]][j] != entrada[1][j]:
                qt_letras_erradas += 1
        if qt_letras_erradas >= 2:
            ass_falsas += 1


    print(ass_falsas)
