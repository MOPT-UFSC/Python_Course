def matriz_de_zeros(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(0)
        matriz.append(linha)
    return matriz


def multiplica_matrizes(m1, m2):
    tamanho = len(m1)
    resultado = matriz_de_zeros(tamanho)

    for i in range(tamanho):
        for j in range(tamanho):
            for k in range(tamanho):
                resultado[i][j] += m1[i][k] * m2[k][j]

    return resultado


if __name__ == "__main__":
    matriz_1 = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
    ]

    matriz_2 = [
        [9, 10, 11],
        [12, 13, 14],
        [15, 16, 17],
    ]

    resultado = [
        [42, 45, 48],
        [150, 162, 174],
        [258, 279, 300],
    ]

    a = multiplica_matrizes(matriz_1, matriz_2)

    assert a == resultado
