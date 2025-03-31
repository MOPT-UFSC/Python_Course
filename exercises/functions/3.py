def mse_0(sinal_a, sinal_b):
    acumulador = 0
    tamanho = len(sinal_a)

    for i in range(tamanho):
        acumulador += (sinal_a[i] - sinal_b[i]) ** 2
    
    return acumulador


def mse_1(sinal_a, sinal_b):
    acumulador = 0
    for a, b in zip(sinal_a, sinal_b):
        diferenca = a - b
        acumulador += diferenca * diferenca
    return acumulador


def mse_2(sinal_a, sinal_b):
    return sum(((a - b) * (a - b) for a, b in zip(sinal_a, sinal_b)))


if __name__ == "__main__":
    from random import randint

    for i in range(100):
        tamanho = randint(1, 20)
        sinal_a = [randint(0, 100) for _ in range(tamanho)]
        sinal_b = [randint(0, 100) for _ in range(tamanho)]

        a = mse_0(sinal_a, sinal_b)
        b = mse_1(sinal_a, sinal_b)
        c = mse_2(sinal_a, sinal_b)

        assert a == b == c