while True:
    try:
        n = input()

        frequencia = [0] * 10

        for i in n:
            frequencia[int(i)] += 1

        index_maior = 0
        for i in range(len(frequencia)):
            if frequencia[index_maior] <= frequencia[i]:
                index_maior = i
        print(index_maior)

    except EOFError:
        break